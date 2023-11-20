from dataclasses import dataclass, fields

@dataclass
class Header:
    id: str
    qr: str
    opcode: str
    aa: str
    tc: str
    rd: str
    ra: str
    z: str
    rcode: str
    qdcount: str
    ancount: str
    nscount: str
    arcount: str


@dataclass
class Question:
    qtype: str
    qclass: str


def message_builder(header: Header, question: Question):
    bit_str = ""
    for field in fields(header):
        field_name = field.name
        if(field_name=="id"):
            continue
        if(field_name=="qdcount"):
            bit_str = format(int(bit_str, 2), '04x')
        field_value = getattr(header, field_name)
        bit_str += field_value

    query= ""
    for field in fields(question):
        field_name = field.name
        field_value = getattr(question, field_name)
        query += field_value

    id = getattr(header, "id")
    message = id + bit_str
    return message, query

def encode_domain(domain):
    encoded_name = b""
    labels = domain.split('.')
    for label in labels:
        encoded_name += bytes([len(label)])
        encoded_name += label.encode()
    encoded_name += b"\x00"
    return encoded_name.hex()
