import time

import gevent
from gevent import monkey

monkey.patch_all()

def f1(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        time.sleep(0.5)

def f2(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        time.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        time.sleep(0.5)

gevent.joinall([gevent.spawn(f1,10),gevent.spawn(f2,10),gevent.spawn(f3,10)])

