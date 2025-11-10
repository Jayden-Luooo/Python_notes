"""
掌握使用continue和break关键字控制循环

continue关键字用于:中断本次循环,接进入下一次循环
continue可以用于:for循环和while循环,效果一致
break的作用是:直接结束所在的循环

continue:临时中断
break:永久中断

注意事项：
continue和break,在for和while循环中作用一致
在嵌套循环中,只能作用在所有的循环上,无法对上层循环起作用

for i in range(1,100):
    语句1
    continue
    语句2
"""
# 演示循环中的断语句continue
# for i in range(1,6):
#         print("语句2")
#         continue
#         print("语句3")

# 演示continue的嵌套应用
# for j in range(1,6):
#     print("语句1")
#     for i in range(1,6):
#         print("语句2")
#         continue
#         print("语句3")
#     print("语句4")

# 演示循环中断语句break
# for i in range(1,100):
#     print("语句1")
#     break #从这里开始无论还剩多少次关于i的循环都断掉，直接从“语句3”开始
#     print("语句2")
# print("语句3")

# 演示break的嵌套应用
for i in range(1,10):
    print("语句1")
    for j in range(1,10):
        print("语句2")
        break
        print("语句3")
    print("语句4")
print("语句5")


