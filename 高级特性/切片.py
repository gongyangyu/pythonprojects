L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])  # L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# 如果第一个索引是0，还可以省略：
print(L[:3])
print(L[1:3])  # 也可以从索引1开始，取出2个元素出来：
print(L[-2:])  # 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
print(L[-2:-1])
# L[-2:0] L[-2:1] 错误 同时为负数
L = list(range(100))
print(L)
print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2])
print(L[:20:5])
print(L[::5])
print(L[:])  # 复制

t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t[:3])
print(t[-2:])
print(t[:6:2])
print(t[::3])
print(t[::])
str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(str[:3])
print(str[::2])
print(str[-3:])

