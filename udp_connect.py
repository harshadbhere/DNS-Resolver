import socket

BUFFER_SIZE = 1024
def udp_connection(msg_query, ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ip, port)
    client_socket.sendto(bytes.fromhex(msg_query), server_address)
    response, server_address = client_socket.recvfrom(BUFFER_SIZE)
    response = response.hex()
    client_socket.close()
    return response
