# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def f(x,y,fp):
    return fp(x)+fp(y)
print(f(-10,34,abs))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
from functools import reduce
def fn(x, y):
    return x*10+y
print(reduce(fn, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

def char2num(s):
     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
     return digits[s]
reduce(fn, map(char2num, '13579'))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def normalize(name):
    def toLower(x):
        if ord(x)>=65 and ord(x)<=90:
            return chr(ord(x)+32)
        return x
    def toUpper(x):
        if ord(x)>=97 and ord(x)<=131:
            return chr(ord(x)-32)
        return x
    def addChr(x,y):
        return str(x)+str(y)
    la=reduce(addChr,map(toLower,name[1:]))
    fi=toUpper(name[0:1])
    return addChr(fi,la)




# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#
# def prod(L):
#     def mul(x,y):
#         return x*y
#     return reduce(mul,L)
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')
#
# print("45"+"abd")


# -*- coding: utf-8 -*-

from functools import reduce
def str2float(s):
    ma={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    l=len(s)
    toInt
    def m(x,y):
        ma(x)
    reduce()



print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')