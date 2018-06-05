import socket
import threading
import time

def socket_server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    host = '127.0.0.1'
    port = 9881

    server.bind((host,port))

    server.listen(5)

    while True:
        sock,add = server.accept()

        print(add)
        t = threading.Thread(target=tcp_link ,args=(sock,add))
        t.start()

def tcp_link(socket,address):
    print('[SERVER]','Accept new connection from %s:%s'% address)
    socket.send('欢迎进入服务器...'.encode('utf-8'))
    while True:
        data = socket.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        socket.send(('Hello %s'% data.decode('utf-8')).encode('utf-8'))
        time.sleep(1)
    socket.close()
    print("connect closed!")

if __name__ == '__main__':
    socket_server()