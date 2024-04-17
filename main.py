import selectors
import socket
import datetime


def accept(sock):
    client, addr = sock.accept()
    client.setblocking(False)
    print(f'Connection accepted from {addr}')
    message = 'Connection confirmed. Server time - {}\r\n'.format(
        datetime.datetime.now().strftime("%H:%M:%S")
    )
    client.sendall(message.encode())
    selector.register(client, selectors.EVENT_READ, client_read)


def client_read(sock):
    message = sock.recv(1024)
    print(f'Client {sock.getpeername()} sent: {message}')
    sock.sendall('Your data recieved\r\n'.encode())


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostport = ('localhost', 7777)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server_socket.bind(hostport)
server_socket.setblocking(False)
server_socket.listen()

selector = selectors.DefaultSelector()
selector.register(server_socket, selectors.EVENT_READ, accept)

while True:
    events = selector.select(timeout=1)
    if len(events) < 1:
        print('No events yet')
    else:
        for key, _ in events:
            func = key.data
            func(key.fileobj)
