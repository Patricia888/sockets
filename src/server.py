# instructions

Construct a socket server that will accumulate a message from some client and return that exact message back to the client.
When the server first starts, a message should be printed to the console of the format "--- Starting server on port 8888 at 12:43:08 29/01/2018 ---"
When the server is stopped, the user shouldn't see any error message.
When the server is stopped, a message should be printed to the console of the format --- Stopping server on port 8888 at 12:43:39 29/01/2018 ---
Whenever a message is received by the server, the server prints to the console a log of that message. It doesn't have to match this exactly, but it should be something like: [12:43:10 29/01/2018] Echoed: 'Hello, world!'


# today

import socket
from datetime import date





# demo

import socket
sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)
sock
address = ('127.0.0.1', 3000)
sock.bind(address)
sock
sock.listen(1)
conn, addr = sock.accept()
conn
addr
buffer_length = 8
message_complete = False
while not message_complete:
    part = conn.recv(buffer_length)
    print(part.decode('utf8'))
    if len(part) < buffer_length:
        break
message = 'thanks for the note'
conn.sendall(message.encode('utf8'))
conn.send??
conn.sendall??
while not message_complete:
    part = conn.recv(buffer_length)
    print(part.decode('utf8'))
    if len(part) < buffer_length:
        break
conn.close()
sock.close()
history
