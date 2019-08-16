import socket

# defaulted to listen on all local address
host = ''
port = 2000

s = socket.socket()
s.bind((host, port))

while True:
    s.listen(5)
    connection, address = s.accept()

    request = connection.recv(1023)

    print('ip: \n{0}\nrequest:\n{1}'.format(address, request.decode('utf-8')))

    response = b'HTTP/1.1 200 VERY OK\r\n\r\n<h1>Hello World!</h1>'
    connection.sendall(response)
    connection.close()
