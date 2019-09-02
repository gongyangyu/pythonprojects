import socket

def main():
    #创建套接字
    socket_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #连接
    addr=input("服务器地址：")
    port=int(input("服务器端口："))
    socket_client.connect((addr,port))
    #发送数据
    file_name=input("请输入文件名：")
    socket_client.send(file_name.encode("gbk"))
    #下载文件
    recv_data=socket_client.recv(1024*1024)
    if recv_data:
        with open("【下载】"+file_name,"wb") as f:
            f.write(recv_data)

    #关闭套接字
    socket_client.close()
if __name__=="__main__":
    main()