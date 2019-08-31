import socket


def main():
    #创建tcp套接字
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定端口
    tcp_server_socket.bind(("",8093))
    tcp_server_socket.listen(128)
    new_client_socket,client_addr=tcp_server_socket.accept()
    print("地址%s" % str(client_addr))
    recv_data=new_client_socket.recv(1024)
    print("%s 发送的数据 %s" % (str(client_addr),recv_data.decode("gbk")))
    new_client_socket.close()
    tcp_server_socket.close()

if __name__ == "__main__":
    main()