import socket

def main():
    #创建socket对象
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #发送数据
    ip="192.168.0.102"
    port=8080
    send_data=input("请输入数据：")
    udp_socket.sendto(send_data.encode("utf-8"),(ip,port))
    #关闭socket
    udp_socket.close();
if __name__=="__main__":
    main()