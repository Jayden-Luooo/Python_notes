"""
使用while循环，猜数字
"""

import random
num = random.randint(1,100)

count = 0

guess_num = int(input("输入你猜测的数字"))
count += 1
while guess_num != num:
    count += 1
    if guess_num > num:
        print("你猜测的数字偏大")
    else:
        print("你猜测的数字偏小")
    guess_num = int(input("输入你猜测的数字"))

print("恭喜你猜对了")
print(f"你总共猜测了{count}次")