"""
练习案例：发工资

某公司,账户余额有1W元,给20名员工发工资。
1.员工编号从1到20,从编号1开始,依次领取工资,每人可领取1000元
2.领工资时,财务判断员工的绩效分(1-10)(随机生成),如果低于5,不发工资,换下一位
3.如果工资发完了,结束发工资。

提示：
使用循环对员工一次发放工资
continue用于跳过员工,直接结束发工资
随机数可以用 :
import random
num = random.randint(1,10)
"""

# 定义账户余额变量
money = 10000
# for循环对员工发放工资
for i in range(1,21):
    import random
    score = random.randint(1,10)

    if score < 5:
        print(f"员工{i}绩效分为{score},不满足绩效要求，不发工资，下一位。")
        # continue跳过发放
        continue

    # 要判余额足不足
    if money >= 1000:
        money -= 1000
        print(f"员工{i},满足条件发放工资1000,公司账户余额为:{money}")
    else:
        print(f"当前余额为:{money}元，不足以发工资，不发了，下个月再来")
        # break结束发放
        break
