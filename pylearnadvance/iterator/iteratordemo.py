import time
from collections import Iterable
from collections import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.curr_index=0

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_index < len(self.names):
            cur_name=self.names[self.curr_index]
            self.curr_index+=1
            return cur_name
        else:
            raise StopIteration


classmate=Classmate()
classmate.add("lao")
classmate.add("lli")
classmate.add("lucy")

print(isinstance(classmate,Iterable))
print(isinstance(classmate,Iterator))

for name in classmate:
    print(name)
    time.sleep(1)