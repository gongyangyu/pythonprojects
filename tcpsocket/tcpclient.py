import socket

def main():
    #创建tcp套接字
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #连接ip
    tcp_socket.connect(("192.168.0.102",8090))
    #发送数据
    tcp_socket.send("你好时机".encode("gbk"))
    recv_data=tcp_socket.recv(1024)
    print("接收到发送的数据：%s" % recv_data.decode("gbk"))
    tcp_socket.close()
if __name__ == "__main__":
    main()