import socket

remote_host = "www.example.com"
remote_port = 80

clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clnt.connect((remote_host, remote_port))

client.send(b"Hello, tcp-server.py!")

response = clnt.recv(4096)

print(response.decode())
clnt.close()    