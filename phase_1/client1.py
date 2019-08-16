import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 2000
s.connect((host, port))

ip, port = s.getsockname()
print('local ip and port: {0}:{1}'.format(ip, port))

http_request = 'GET / HTTP/1.1\r\nhost:{}\r\n\r\n'.format(host)
request = http_request.encode('utf-8')
print('request', request)
s.send(request)

response = s.recv(1023)

print('response', response)
print('response的 str 格式', response.decode('utf-8'))
