#!/usr/bin/python3

import socket

def socket_client():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #s.setblocking(0)
    host = '116.62.164.196'
    port = 8080
    s.connect((host,port))

    s.send(b"GET /portal/index HTTP/1.1\r\nHost: 116.62.164.196:8080\r\nAccept: */*\r\n Connection: close\r\n\r\n")

    buffer = []
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)

    header,html = data.split(b'\r\n\r\n',1)

    print(header.decode('utf-8'))

    with open('d:/baidu.html','wb') as file:
        file.write(html)

    s.close()

if __name__ == '__main__':
    socket_client()

