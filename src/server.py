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
