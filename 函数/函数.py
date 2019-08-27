from abs_se import self_abs
# print(hex(int('34')))

print(self_abs(-9))
# print(self_abs('d'))
print(type('23'))

# 返回多个值
from game import move
import math
print(move(4,5,2,30))

r = move(100, 100, 60, math.pi / 6)
print(r)

from quadratic import quadratic

print(quadratic(1,-2,1))
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

