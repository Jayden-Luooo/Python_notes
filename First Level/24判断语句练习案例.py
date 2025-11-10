"""
定义一个1~10的数字来猜
"""
# 1.构建一个随机的数字变量
import random
num = random.randint(1,10)

guess_num = int(input("输入你猜测的数字"))

# 2.通过if判断语句进行数字的猜测
if guess_num == num:
    print("恭喜你猜对了！")
else:
    if guess_num > num:
        print("你猜测的数字偏大")
    else:
        print("你猜测的数字偏小")

    guess_num = int(input("输入你猜测的数字"))

    if guess_num == num:
        print("恭喜你猜对了！")
    else:
        if guess_num > num:
            print("你猜测的数字偏大")
        else:
            print("你猜测的数字偏小")

        guess_num = int(input("输入你猜测的数字"))
        
        if guess_num == num:
            print("恭喜你猜对了！")
        else:
            if guess_num > num:
                print("你猜测的数字偏大")
            else:
                    print("你猜测的数字偏小")

            guess_num = int(input("输入你猜测的数字"))

            if guess_num == num:
                print("恭喜你猜对了！")
            else:
                print("这么久都猜不中？")
