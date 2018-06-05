import asyncio
import socket


loop = asyncio.get_event_loop()
CHUNK_SIZE = 1024


async def connect(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    print("%s:%d" % (host, port))
    try:
        await loop.sock_connect(sock, (host, port))
    except (socket.timeout, ConnectionRefusedError):
        pass
    else:
        await loop.sock_sendall(sock, "test\r\n".encode("utf-8"))
        response = b""
        try:
            chunk = await loop.sock_recv(sock, CHUNK_SIZE)
        except (socket.timeout, ConnectionResetError):
            pass
        else:
            while chunk:
                print(chunk)
                response += chunk
                chunk = await loop.sock_recv(sock, CHUNK_SIZE)
    finally:
        sock.close()


def main():
    host_name_list = ["www.baidu.com", "cn.bing.com", "www.acfun.tv", "www.bilibili.com", "www.zhihu.com"]
    host_list = [socket.gethostbyname(name) for name in host_name_list]
    port_list = [23, 45, 123, 22, 55, 666, 77, 88, 99, 1010,1 ,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    tasks = asyncio.gather(*[connect(host, port) for host in host_list for port in port_list])
    loop.run_until_complete(tasks)
    loop.close()


if __name__ == "__main__":
    main()