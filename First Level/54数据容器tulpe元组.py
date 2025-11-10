"""
tulpe 元组
列表是可以被修改的
元组一旦定义完成就不可修改——可以防止数据篡改

# 定义元组字面量
(元素,元素,元素,...元素)

# 定义元组变量
变量名称 = (元素,元素,元素,...元素)

# 定义空元组
变量名称 = ()       # 方式1
变量名称 = tuple()  # 方式2
"""

# 定义元组
t1 = (1,"Hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是:type{type(t1)},内容是:{t1}")
print(f"t1的类型是:type{type(t2)},内容是:{t2}")
print(f"t1的类型是:type{type(t3)},内容是:{t3}")

# 定义单个元素的元素
t4 = ("hello")
print(f"t4的类型:{type(t4)},t4的类容是:{t4}")

# 元组的嵌套
t5 = ((1,2,3,),(4,5,6))
print(f"t4的类型:{type(t5)},t5的类容是:{t5}")

# 下标索引去取出内容
num = t5[1][2]
print(f"从嵌套元组中取出的数据是:{num}")

# 元组的操作:index查找方法
t6 = ("传智教育","黑马程序员","Python")
xiabiao = t6.index ("黑马程序员")
print(f"在元组t6中,黑马程序员,的下标是:{xiabiao}")

# 元组的操作:count统计方法
t7 = ("传智教育","黑马程序员","Python","传智教育","黑马程序员","Python")
num2 = t7.count ("黑马程序员")
print(f"在元组t7中,黑马程序员的数量为:{num2}")

# 元组的操作:Len函数统计元组元素数量
t8 = ("传智教育","黑马程序员","Python","传智教育","黑马程序员","Python")
num4 = len(t8)
print(f"t8元组中的元素有:{num}个")

# 元组的遍历:while
i = 0
while i < len(t8):
    print(f"while元组的元素有:{t8[i]}")
    # 至关重要
    i += 1

# 元组的遍历:for
j = 0
for j in t8:
    print(f"for元组的元素有:{j}")

# 修改元组内容
# t8[0] = "itcast"
# print(t8)
# 会报错

# 定义一个元组
t9 = (1,2,["itcast","itheima"])
print(f"t9的内容是:{t9}")
t9[2][0] = "传智教育"
t9[2][1] = "黑马程序员"
print(f"t9的内容是:{t9}")

print(t9[1])