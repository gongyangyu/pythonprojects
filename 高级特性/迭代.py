d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print('key',key)
    print('value',d[key])

for ch in 'ABC':
    print(ch)
from collections import Iterable

print(isinstance('abc',Iterable))

print(isinstance([1,2,3], Iterable)) # list是否可迭代
print(isinstance(123, Iterable))

for i,value in enumerate('abc'):
    print(i,value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)

# -*- coding: utf-8 -*-
def findMinAndMax(L):
    min,max=None,None
    for x,y in enumerate(L):
        if x==0:
            min,max=y,y
        if min>y:
            min=y
        if max<y:
            max=y
    return (min,max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')