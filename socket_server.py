#! /usr/bin/python3

import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #定义服务器通信方式
host=socket.gethostbyname('127.0.0.1')
port=5150
server.bind((host,port))
server.listen(5)
print("Listening for a client....")
client,addr=server.accept()  #接收到客户端的连接
print("Acceted connection from :",addr)
client.send(str.encode("welcome to my server!"))
while True:
    data = client.recv(1024) #从客户端接收
    if(bytes.decode(data)=='exit'):
        break
    else:
        print('Received data from client:',bytes.decode(data))
        client.send(data)#向客户端发送数据
print('Ending the connection')
client.send(str.encode('exit'))
client.close()
