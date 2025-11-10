"""
int(x)   将x转换为一个整数
float(x) 将x转换为一个浮点数
str(x)   将x转换为一个字符串
"""
# 将数字类型转换成字符串
num_str = str(11)
print(type(num_str), num_str)

# 将浮点数传换成字符串
float_str = str(13.14)
print(type(float_str), float_str)

# 将字符串转换成数字
num = int("11")
print(type(num), num)

num2 = float("13.145")
print(type(num2), num2)

#数字和浮点数可以转换成字符串，但是想要字符串转换成数字或者浮点数，字符串里必须是数字

# 这里的结果只会显示1，因为int转换成float会失去精度
int_num = int(1.323)
print(type(int_num), int_num)

