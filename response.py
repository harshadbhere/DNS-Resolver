from dns import message

def decode_dns_response(hex_string):
    byte_data = bytes.fromhex(hex_string)
    dns_msg = message.from_wire(byte_data)
    if len(dns_msg.answer)>0:
        ans_list = []
        for i in (dns_msg.answer[0].items):
            ip_address = i.to_text()
            print(ip_address)
        return 0, []

    else:
        if len(dns_msg.authority)>0:
            authority_list = []
            for i in dns_msg.authority[0].items:
                ns_record = i.target.to_text()
                authority_list.append(ns_record)
            # print(authority_list)

            additional_list = []
            for i in dns_msg.additional:
                if i.rdtype:
                    t = i.to_text().split()
                    if t[3] == 'A':
                        additional_list.append(t[4])
            return 1, additional_list