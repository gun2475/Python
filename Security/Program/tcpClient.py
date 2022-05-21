import socket
HOST = '0.0.0.0'
PORT = 9998
# socket object create
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client connect
client.connect((HOST,PORT))
# send arbitrary data
client.send(b'GET / HTTP/1.1\R\nHost: google.com\r\n\r\n')
# receive response data
response = client.recv(4096)
print(response.decode('utf-8'))
client.close()