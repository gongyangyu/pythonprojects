import socket

def main():
    #创建套接字
    tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #连接端口
    tcp_server.bind(("",7788))
    #监听客户端
    tcp_server.listen(128)

    #为多个客户端服务
    while True:
        print("等待客户端连接")
        new_tcp_client,client_addr=tcp_server.accept()
        print("新连接的客户端%s" % str(client_addr))

        #为一个客户端服务多次
        while True:
            recv_data=new_tcp_client.recv(1024)
            print("客户端发送的消息：%s" % recv_data.decode("utf-8"))
            if recv_data:
                new_tcp_client.send("**************************\n-------------------------\n***********hello，你好*************\n--------------------------\n*********************************".encode("utf-8"))
            else:
                break
        new_tcp_client.close()
        print("退出连接")
        isexit=input("是否退出？")
        if isexit=="y":
            break
    tcp_server.close()

if __name__=="__main__":
    main()