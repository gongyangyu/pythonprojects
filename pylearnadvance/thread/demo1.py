import threading
import time


def sing():
    """唱歌5s"""
    for i in range(5):
        print("----------正在唱歌----------")
        time.sleep(1)


def dance():
    """跳舞5s"""
    for i in range(5):
        print("----------正在跳舞----------")
        time.sleep(1)


def main():
    t1=threading.Thread(target=sing)
    t2=threading.Thread(target=dance)
    t1.start()
    t2.start()


if __name__  ==  "__main__":
    main()