"""
None类型 <class'NoneType'>
None表示：空的、无意义的意思
"""
# 无return语句的函数返回值
def say_hi():
    print("你好呀！")

result = say_hi()
print(f"无返回值函数，返回的内容是:{result}")
print(f"无返回值函数，返回的内容类型是:{result}")

# 主动返回None的函数
def say_hi2():
    print("你好呀！")
    return None

result = say_hi2()
print(f"无返回值函数，返回的内容是:{result}")
print(f"无返回值函数，返回的内容类型是:{result}")

# None用于if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None

result = check_age(16)
if not result:  # 进入if表示result是None值，也就是Flase
    print("未成年，不可以进入")

# None用于声明无初始内容的变量
name = None # 先不赋值，所以先用None代替
print(f"{name}")


