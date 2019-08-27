def trim1(s):
    print('start:',s)
    if s=="":
        print("")
        return s
    b=True
    while b:
        if s[:1]==" ":
            l=len(s)
            print('length',l)
            s=s[1:l]
            print('1',s)
        elif s[-1:]==" ":
            s=s[-len(s):-1]
            print('2',s)
        else:
            b=False
    print(s)
    return s

# def trim(s):
#     print('start',s)
#     if s=="":
#         return s
#     b=True
#     if s[:1]==" ":
#         b=False
#         s=s[1:len(s)]
#     if s[-1:]==" ":
#         b=False
#         s=s[-len(s):-1]
#     if b:
#         return s
#     return trim(s)

def trim(s):
    if len(s) == 0:
        return s
    if s[0] == ' ':
        return trim(s[1:])
    if s[-1] == ' ':
        return trim(s[:-1])
    return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


print(len("3434"[2:2]))