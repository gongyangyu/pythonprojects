import socket

def main():
    #创建套接字
    socket_udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定地址
    locAddr=("",7788)
    socket_udp.bind(locAddr)
    #接收数据
    recv_data=socket_udp.recvfrom(1024)
    print(recv_data)
    #关闭套接字
    socket_udp.close()

if __name__=="__main__":
    main()