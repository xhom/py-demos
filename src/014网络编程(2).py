# coding=UTF-8

# socket编程
import socket

# client
client = socket.socket()
print '客户端已创建...'
client.connect(("127.0.0.1",8080))
print "已连接到服务端..."
client.send("你好，我是客户端（Client）")
print "收到服务端消息：",client.recv(1024) #接收服务端数据
client.close()