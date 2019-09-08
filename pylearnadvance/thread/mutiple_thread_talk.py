import socket
import threading


def send_msg(udp_socket, remote_addr, remote_port):
    global g_flag
    while True:
        # 输入发送的消息
        print("g_flag:%s" % str(g_flag))
        send_msgstr = input("请输入发送的信息：")
        if g_flag:
            print("send_msg 聊天结束，谢谢")
            break
        if send_msgstr == "exit":
            print("send_msg 聊天结束，谢谢")
            g_flag = True
            udp_socket.close()
            break
        else:
            udp_socket.sendto(send_msgstr.encode("utf-8"), (remote_addr, remote_port))


def recv_msg(udp_socket):
    global g_flag
    while True:
        print("g_flag:%s" % str(g_flag))
        # 接收数据
        if g_flag:
            print("recv_msg 聊天结束，谢谢")
            break
        recv_data = udp_socket.recvfrom(1024)
        print("%s 发来的消息是:%s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))
        if recv_data[0] == b'exit':
            print("recv_msg 聊天结束，谢谢")
            g_flag = True
            udp_socket.close()
            break


g_flag = False


def main():
    """udp聊天"""
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    udp_socket.bind(("", 7788))
    # 输入对方IP
    remote_addr = input("请输入ip地址")
    remote_port = int(input("请输入端口号："))

    t_send = threading.Thread(target=send_msg, args=(udp_socket, remote_addr, remote_port))
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send.start()
    t_recv.start()


if __name__ == "__main__":
    main()
