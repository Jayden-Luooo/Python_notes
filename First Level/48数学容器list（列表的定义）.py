"""
数据容器入门
Python中的数据容器:
·一种可以容纳多份数据的数据类型
·容纳的每一份数据称之为1个元素
·每一个元素,可以是任意类型的数据,如字符串、数字、布尔等。
·元素的数据类型没有任何限制,甚至元素也可以是列表,这样就定义了嵌套列表

·list(列表)、tuple(元组)、str(字符串)、set(集合)、dict(字典)

list:
# 字面量
[元素1,元素2,元素3,元素4,...]

# 定义变量
变量名称 = [元素1,元素2,元素3,元素4,...]
"""

# name_list = ['itheima','itcast','python']
# print(name_list)
# print(type(name_list))

# 定义一个列表list
my_list = ["itheima","itcast","python"]
print(my_list)
print(type(my_list))

my_list = ["itheima", 666, True]
print(my_list)
print(type(my_list))

# 定义一个嵌套的列表
my_list = [[1,2,3],[4,5,6]]
print(my_list)
print(type(my_list))
