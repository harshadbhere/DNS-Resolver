import message_format as mf
import udp_connect as up
import response as res

Header = mf.Header(id="0016", qr="0", opcode="0000", aa="0", tc="0", rd="0", ra="0", z="000", rcode="0000",
                   qdcount="0001", ancount="0000", nscount="0000", arcount="0000")
Question = mf.Question(qtype="0001", qclass="0001")

host_name = "geeksforgeeks.org"
message, query = mf.message_builder(Header, Question)
domain = mf.encode_domain(host_name)
request = message + domain + query

ips = ["192.203.230.10"]
port = 53

for ip in ips:
    response = up.udp_connection(request, ip, port)
    response_id = response[0:4]
    if(response_id!=Header.id):
        print("Invalid request response")
    else:
        # flags = response[4:8]
        # question = response[8:12]
        # answer = response[12:16]
        # authority = response[16:20]
        # additional = response[20:24]
        # qname_length = len(domain)
        # ptr = response.find(domain)
        # ptr = ptr + qname_length
        # qtype = response[ptr:ptr+4]
        # qclass = response[ptr+4:ptr+8]
        # response_info = response[ptr+8:]
        print("Querying", ip, "for", host_name)
        ns, lst = res.decode_dns_response(response)
        if ns==0:
            break
        ips.extend(lst)