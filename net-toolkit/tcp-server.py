import socket
import threading

IP = '0.0.0.0'
PORT = 8888

def main():
    svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    svr.bind((IP, PORT))
    svr.listen(5)

    print(f'*** Listening on (IP):(PORT) ***')

    while True:
        client, address = svr.accept()
        print(f'Connection received from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

    def handle_client(client_socket):
        with client_socket as sck:
            request = sck.recv(1024)
            print(f'*** Received: {request.decode("utf-8")} ***')
            sck.send(b'ACK')

    if __name__ == '__main__':
        main()







