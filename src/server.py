# # instructions

# Construct a socket server that will accumulate a message from some client and return that exact message back to the client.
# When the server first starts, a message should be printed to the console of the format "--- Starting server on port 8888 at 12:43:08 29/01/2018 ---"
# When the server is stopped, the user shouldn't see any error message.
# When the server is stopped, a message should be printed to the console of the format --- Stopping server on port 8888 at 12:43:39 29/01/2018 ---
# Whenever a message is received by the server, the server prints to the console a log of that message. It doesn't have to match this exactly, but it should be something like: [12:43:10 29/01/2018] Echoed: 'Hello, world!'


# today

import socket
from datetime import datetime

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)
PORT = 3000
address = ('127.0.0.1', PORT)
sock.bind(address)
try:
    sock.listen(1)
    daytime = datetime.now().strftime("%H:%M:%S %d/%m/%y")
    print('--- Starting server on port {} at {} ---'.format(PORT, daytime))
    conn, addr = sock.accept()

    buffer_length = 8
    message_complete = False
    message = b''
    while not message_complete:
        part = conn.recv(buffer_length)
        message += part
        # print(part.decode('utf8'))
        if len(part) < buffer_length:
            break
    message = message.decode('utf8')
    print(daytime, 'Echoed: ', message)
    conn.sendall(message.encode('utf8'))
    # while not message_complete:
    #     part = conn.recv(buffer_length)
    #     # write echo
    #     print('[{}] Echoed: ', part.decode('utf8'))
    #     if len(part) < buffer_length:
    #         break

    stopServer = datetime.now().strftime("%H:%M:%S %d/%m/%y")
    print('--- Stopping server on port {} at {} ---'.format(PORT, stopServer))
    conn.close()
    sock.close()

except KeyboardInterrupt:
    try:
        conn.close()
    except NameError:
        pass

    sock.close()
    stopServer = datetime.now().strftime("%H:%M:%S %d/%m/%y")
    print('--- Stopping server on port {} at {} ---'.format(PORT, stopServer))





# demo
'''
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
'''