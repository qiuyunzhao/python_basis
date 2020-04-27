# 通过类型检查，可以检查（变量）的类型
a = 123  # 数值
b = '123'  # 字符串
print('a =', a)
print('b =', b)

# type()用来检查值的类型，该函数会将检查的结果作为返回值返回，可以通过变量来接收函数的返回值
print(type(1))  # <class 'int'>
print(type(1.5))  # <class 'float'>
print(type(True))  # <class 'bool'>
print(type('r_单元测试'))  # <class 'str'>
print(type(None))  # <class 'NoneType'>

# ==============================================================================================
# 类型转换四个函数 int() float() str() bool()

# int() 可以用来将其他的对象转换为整型
#       规则：
#         布尔值：True -> 1   False -> 0
#         浮点数：直接取整，省略小数点后的内容
#         字符串：合法的整数字符串，直接转换为对应的数字
#                 如果不是一个合法的整数字符串，则报错 ValueError: invalid literal for int() with base 10: '11.5'
#         对于其他不可转换为整型的对象，直接抛出异常 ValueError

# float() 和 int()基本一致，不同的是它会将对象转换为浮点数

# str() 可以将对象转换为字符串
#       True -> 'True'
#       False -> 'False'
#       123 -> '123'
#
# bool() 可以将对象转换为布尔值，任何对象都可以转换为布尔值
#       规则：对于所有表示空性的对象都会转换为False，其余的转换为True
#          哪些表示的空性：0 、 None 、 ''、...

# int()函数不会对原来的变量产生影响，他是对象转换为指定的类型并将其作为返回值返回
# 如果希望修改原来的变量，则需要对变量进行重新赋值
a = True
a = int(a)  # 1
a = False
a = int(a)  # 0

a = '123'
a = int(a)  # 123

a = 11.6
a = int(a)  # 11

a = '11.5'
a = int(a)  # 不是一个合法的整数字符串 ValueError

a = None
a = int(a)  # 不可转换为整型的对象

a = 1
a = float(a)  # 1.0

a = False
a = float(a)  # 0.0

a = 123
a = str(a)

a = None
a = bool(a) # False

print('a =', a)
print('a的类型是', type(a))

b = 456
print('r_单元测试'+str(b))
