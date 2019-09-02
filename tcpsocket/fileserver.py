import socket

def main():
    #创建套接字
    file_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定地址
    file_server.bind(("",7878))
    #监听
    file_server.listen(128)
    #接收
    file_client,client_addr=file_server.accept()

    file_name=file_client.recv(1024).decode("gbk")
    print("%s 下载的文件%s" % (str(client_addr),file_name))
    file_content=None
    try:
        f=open(file_name,"rb")
        file_content=f.read()
        f.close()
    except Exception as e:
        print("没有要下载的文件 %s" % file_name)
    file_client.send(file_content)


if __name__=="__main__":
    main()