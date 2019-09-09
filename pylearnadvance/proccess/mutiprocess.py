import multiprocessing
import time
def test1():
    for i in range(1000000):
        time.sleep(0.01)
        print("test1:%s" % str(i))
def test2():
    for i in range(1000000):
        time.sleep(0.01)
        print("test2:%s" % str(i))

def main():
    p1=multiprocessing.Process(target=test1)
    p2=multiprocessing.Process(target=test2)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()