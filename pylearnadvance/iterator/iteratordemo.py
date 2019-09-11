import time
from collections import Iterable
from collections import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()


    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        return Classiterator()

class Classiterator(object):
    def __iter__(self):
        pass
    def __next__(self):
        return 11

classmate=Classmate()
classmate.add("lao")
classmate.add("lli")
classmate.add("lucy")

print(isinstance(classmate,Iterable))
print(isinstance(classmate,Iterator))

for name in classmate:
    print(name)
    time.sleep(1)