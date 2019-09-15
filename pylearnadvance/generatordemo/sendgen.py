def create_num(all):
    a,b=0,1
    cur_num=0
    while cur_num<all:
        ret = yield a
        print('------>',ret)
        a,b=b,a+b
        cur_num+=1

obj=create_num(10)

ret=next(obj)
print(ret)

ret=obj.send(None)
print(ret)

ret=obj.send("----hfafd---")
print(ret)

ret=next(obj)
print(ret)


