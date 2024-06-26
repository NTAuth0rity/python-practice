import socket

remote_host = "127.0.0.1"
remote_port = 8888

clnt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clnt.sendto(b"*** UDP packets received. ***")

data, addr = clnt.recvfrom(4096)

print(data.decode())
client.close()