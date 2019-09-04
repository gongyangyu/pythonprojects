import threading


g_num=100


def test1():
    global g_num
    g_num+=1
    print("-------g_num ---test1 %d" % g_num)


def test2():
    print("-----g_num----test2 %d" % g_num)


def main():
    t1=threading.Thread(target=test1)
    t2=threading.Thread(target=test2)
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()