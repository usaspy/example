#!/usr/bin/python3

import socket

def socket_client():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #s.setblocking(0)
    host = '127.0.0.1'
    port = 9881
    s.connect((host,port))

    print(s.recv(1024).decode("utf-8"))

    for data in ['王老五','李斯','张三']:
        s.send(data.encode("utf-8"))
        print(s.recv(1024).decode("utf-8"))
    s.send(b'exit')
    s.close()

if __name__ == '__main__':
    socket_client()

