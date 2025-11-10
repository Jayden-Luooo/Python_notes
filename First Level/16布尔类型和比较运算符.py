"""
掌握布尔(bool)类型用于表示：真和假 True and False
掌握比较运算符用于计算：真和假
变量名称 = 布尔类型字面量

"""
# 定义变量存储布尔类型的数据 True & False
bool_1 = True
bool_2 = False
print(f"boo_1变量的内容是：{bool_1}, 类型是: {type(bool_1)}")
print(f"boo_2变量的内容是：{bool_2}, 类型是: {type(bool_2)}")
# 比较运算符的使用
# == != > < >= <=
# 演示进行内容的相等比较
num1 = 10
num2 = 10
print(f" 10 = 10的结果是 {num1 == num2}")
# 相等所以是True

num1 = 10
num2 = 15
print(f" 10 = 10的结果是 {num1 != num2}")
# 不相等所以是True

name1 = "itcast"
name2 = "itheima"
print(f"name1 = name2的结果是{name1 == name2}")
# 不相等所以是False

# 演示大于小于，大于等于小于等于的比较运算
num1 = 10
num2 = 5
print(f"10 > 5的结果是：{num1 > num2}")
print(f"10 < 5的结果是：{num1 < num2}")

num1 = 10
num2 = 10
print(f"10 >= 10的结果是：{num1 >= num2}")
print(f"10 <= 10的结果是：{num1 <= num2}")
