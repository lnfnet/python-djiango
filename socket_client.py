#!/usr/bin/python3

import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #定义服务器通信方式
host=socket.gethostbyname('localhost')
port = 5150

server.connect((host,port))   #发起连接服务器
data=server.recv(1024) #接收1024个字节数据 
print(bytes.decode(data))
while True:
    data=input("Enter text to send:")
    server.send(str.encode(data))
    data=server.recv(1024)
    print('Received from server:',bytes.decode(data))
    if(bytes.decode (data)=='exit'):
        break
print('closing connection')
server.close()
