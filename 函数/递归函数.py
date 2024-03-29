def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(100))
# 如果一个函数在内部调用自身本身，这个函数就是递归函数
# print(fact(1000))
# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
#
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
#
# 上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：

def fact_tail(n,product):
    if n==1:
        return product
    else:
        product*=n
    return fact_tail(n-1,product)

# print(fact(1000))

# -*- coding: utf-8 -*-
def move(n, a, b, c):
    if n==1:
        print(a,'-->',c)
        return
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
        return

move(3,'A','B','C')