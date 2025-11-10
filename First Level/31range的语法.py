"""
for循环的基础语法---range
"""

"""
, end='' 代表着不换行
"""
# range语法1 range(num)
range(10)
for x in range(10):
    print(x, end='')
print()

# range语法2 range(num1,num2)
for y in range(5,10):
    # 从5开始，到10结束（不包含10本身）的一个数字序列
    print(y, end='')
print()

# range语法3 range(num1,num2,step) step在这里是步长
for z in range(5,20,2):
    # 从5开始，到20结束（不包含20本身）的一个数字序列，数字之间的间隔是2(step)
    print(z, end='')

for r in range(10):
    print("送玫瑰花")