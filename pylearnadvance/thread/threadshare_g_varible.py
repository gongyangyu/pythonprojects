import threading
import time


def test1(temp):
    temp.append(34)
    print("-------g_num ---test1 %s" % str(temp))


def test2(temp):
    print("-------g_num ---test2 %s" % str(temp))


g_num=[23,24]

def main():
    t1=threading.Thread(target=test1,args=(g_num,))
    t2=threading.Thread(target=test2,args=(g_num,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)

    print("-------g_num ---main %s" % str(g_num))

if __name__ == "__main__":
    main()