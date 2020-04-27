# 1.普通函数定义
def mySum1(a, b, c):
    return a + b + c


# 2.形参带默认值
#     默认值要放在形参最后
def mySum2(a, b=2, c=3):
    print('a=', a, 'b=', b, 'c=', c)
    return a + b + c


# 3.返回值
#     return 后边可以跟任意的对象，返回值甚至可以是一个函数
#     不写return语句或return后无内容 返回值为None
def fn():
    # return 'Hello'
    # return [1, 2, '3'] # 返回列表
    # return 1, 2, '3'  # 返回元组
    # return {'k': 'v'} # 返回字典
    def fn2():
        print('r_单元测试')

    return fn2  # 返回值也可以是一个函数


print('------------------------------------------------------------.函数调用')
# 函数在调用时，解析器不会检查实参的类型，实参可以传递任意类型的对象

# fn是函数对象  fn()调用函数
print(mySum1, id(mySum1), type(mySum1))

# 实参传递方式
# 方式一：位置参数
sum_result2 = mySum2(1, 2)
print(sum_result2)
# 方式二：关键字参数
sum_result2 = mySum2(c=10, b=30, a=20)
print(sum_result2)
# 方式三：混合方式    注：位置参数必须在关键字参数前边
sum_result2 = mySum2(100, b=30)
print(sum_result2)

# 返回值
r = fn()
r()
print(r, type(r))
