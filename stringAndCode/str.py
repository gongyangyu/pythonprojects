# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
print('包含中文的str')
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
# 如果知道字符的整数编码，还可以用十六进制这么写
print( '\u4e2d\u6587')
x=b'ABC'
print(x)
print(x.decode('ascii'))
y= '中文'.encode('utf-8')
print(y)
print(y.decode('utf-8'))
print(b'AfffddBC'.decode('ascii'))
print( len('ABC'))