# coding=UTF-8

# socket编程
import socket

# server
server = socket.socket()
print "服务端已创建..."
server.bind(('127.0.0.1', 8080))
print "服务端地址端口已绑定..."
server.listen(5)
print "开始监听客户端连接..."
while True:
    client, addr = server.accept() # 阻塞式函数
    client.send("你好，我是服务端（Server）")
    print "收到客户端"+str(addr)+"消息：", client.recv(1024)
    client.close()

