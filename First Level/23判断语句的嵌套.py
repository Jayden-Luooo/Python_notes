"""
嵌套的使用
"""

if int(input("你的身高是多少：")) > 120:
    print("身高超出限制，不可以免费")
    print("但是，如果vip级别大于3，可以免费")

    if int(input("你的vip等级是多少：")) > 3:
        print("恭喜你，vip级别达标，可以免费")
    else:
        print("恭喜你不能免费进去，需要购票10元")
else:
    print("你好小朋友，你可以免费进")



