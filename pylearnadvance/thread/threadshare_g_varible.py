import threading
import time


total=0

def test1(number):
    global total
    for i in range(number):
        mutex.acquire()
        total+=1
        mutex.release()
    print("-------g_num ---test1 %s" % str(total))


def test2(number):
    global total
    for i in range(number):
        mutex.acquire()
        total+=1
        mutex.release()
    print("-------g_num ---test2 %s" % str(total))


g_num=10000000
mutex=threading.Lock()


def main():
    t1=threading.Thread(target=test1,args=(g_num,))
    t2=threading.Thread(target=test2,args=(g_num,))
    t1.start()
    t2.start()

    time.sleep(35)
    print("-------g_num ---main %s" % str(total))

if __name__ == "__main__":
    main()