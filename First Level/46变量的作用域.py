"""
变量作用域指的是变量的作用范围(变量在哪里可用,在哪里不可用)
主要分为两类:局部变量和全局变量

所谓局部变量是定义在函数体内部的变量，即只在函数体内部生效
"""
# 演示局部变量
def test_a():
    num = 100
    print(num)

test_a()
# 出了函数体，局部变量就无法正常使用了
# 所以这里不能写 print(num)

# 演示全局变量
num1 = 200
def test_b():
    print(f"test_b():{num1}")

def test_c():
    print(f"test_c():{num1}")

test_b() # 结果：200
test_c() # 结果：200
print(num1) # 结果：全局变量num = 200

# 在函数内修改全局变量
num2 = 200
def test_d():
    print(f"test_d():{num2}")

def test_e():
    num2 = 500 # 在这里将num1修改为了500
    print(f"test_e():{num2}")

test_d() # 结果：200
test_e() # 结果：500
print(num2) # 但是外层的num1依然是200

# 使用global关键字，在函数内声明变量为全局变量
num3 = 200
def test_f():
    print(f"test_f():{num3}")

def test_g():
    global num3 # 设置内部定义的变量为全局变量
    num3 = 500 
    print(f"test_g():{num3}")

test_f()
test_g()
print(num3) # 在执行test_g()的时候将num3换成了500 所以输出的全局变量为500
