# 作用域（scope）
#
# 在Python中一共有两种作用域
#  全局作用域
#   - 全局作用域在程序执行时创建，在程序执行结束时销毁
#   - 所有函数以外的区域都是全局作用域
#   - 在全局作用域中定义的变量，都属于全局变量，全局变量可以在程序的任意位置被访问
#
#  函数作用域
#   - 函数作用域在函数调用时创建，在调用结束时销毁
#   - 函数每调用一次就会产生一个新的函数作用域
#   - 在函数作用域中定义的变量，都是局部变量，它只能在函数内部被访问
#
#  变量的查找
#   - 当我们使用变量时，会优先在当前作用域中寻找该变量，如果有则使用，
#       如果没有则继续去上一级作用域中寻找，如果有则使用，
#       如果依然没有则继续去上一级作用域中寻找，以此类推
#       直到找到全局作用域，依然没有找到，则会抛出异常
#           NameError: name 'a' is not defined

outer_var = 20  # 全局变量


def fn():
    inner_var = 10  # 函数内部变量
    print('函数内部：', 'inner_var =', inner_var)
    print('函数内部：', 'outer_var =', outer_var)


fn()


def fn3():
    # 在函数内部修改全局变量，则需要使用global关键字，来声明变量
    global outer_var  # 声明使用的outer_var是全局变量，修改outer_var，就是在修改全局的outer_var
    outer_var = 100  # 修改全局变量
    print('函数内部：', 'outer_var =', outer_var)


fn3()
print('函数外部：', 'outer_var =', outer_var)

# =============================================================================================

# 命名空间（namespace）
#
#   命名空间指的是变量存储的位置，每一个变量都需要存储到指定的命名空间当中
#   每一个作用域都会有一个对应的命名空间
#   全局命名空间，用来保存全局变量。函数命名空间，用来保存函数中的变量
#   命名空间实际上就是一个字典，是一个专门用来存储变量的字典

# locals() 用来获取当前作用域的命名空间
#   在全局作用域中调用locals()则获取全局命名空间，在函数作用域中调用locals()则获取函数命名空间
#   返回的是一个字典

scope = locals()  # 在全局作用域中调用locals()则获取全局命名空间
print(type(scope), '----', scope)

a = '孙悟空'
print(a)
print(scope['a'])

# 向scope中添加一个key-value,就相当于在全局中创建了一个变量（一般不建议这么做）
scope['c'] = 1000
print(c)


def fn4():
    scope = locals()  # 在函数内部调用locals()会获取到函数的命名空间
    print(type(scope), '----', scope)

    global_scope = globals()  # globals() 函数可以用来在任意位置获取全局命名空间
    print(global_scope['a'])  # 获取全局变量
    global_scope['a'] = 30  # 修改全局变量


fn4()
print(a)
