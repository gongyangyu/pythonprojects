import time

from greenlet import greenlet


def t1():
    while True:
        print("----a---")
        gr2.switch()
        time.sleep(0.5)

def t2():
    while True:
        print("----b---")
        gr1.switch()
        time.sleep(0.5)

gr1=greenlet(t1)
gr2=greenlet(t2)

gr1.switch()

