import socket


def main():
    # 创建套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 绑定
    dest_ip=input("请输入ip：")
    dest_port=int(input("请输入port："))
    udp_socket.bind(("",7788))
    while True:
        send_data=input("请输入发送信息：")
        # 接收数据
        udp_socket.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))
        recv_data=udp_socket.recvfrom(1024)
        print("%s 发送的数据：%s" % (str(recv_data[1]),recv_data[0].decode("utf-8")))
        if send_data=="over":
            break
    # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
