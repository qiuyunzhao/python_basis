# 定义：将函数作为返回值返回，也是一种高阶函数叫做闭包
# 功能：可以访问函数内部的变量，并将一些私有的数据藏到的闭包中


# =============================================== 常规函数 ==============================================
numbers = []  # 创建一个列表，用来保存数值，对外隐藏


def my_averager(n):
    numbers.append(n)  # 将n添加到列表中
    return sum(numbers) / len(numbers)  # 求平均值


# 可以访问到 numbers 可能会被意外修改
print(my_averager(10))
print(my_averager(20))
print(my_averager(30))
numbers = []
print(my_averager(40))


# =============================================== 闭包 ==============================================

#  形成闭包的要件
#   ① 函数嵌套
#   ② 将内部函数作为返回值返回
#   ③ 内部函数必须要使用到外部函数的变量

def make_averager():
    nums = []  # 创建一个列表，用来保存数值，对外隐藏

    # 创建一个函数，用来计算平均值
    def averager(n):
        nums.append(n)  # 将n添加到列表中
        return sum(nums) / len(nums)  # 求平均值

    return averager


averager = make_averager()

# 访问不到 nums 可防止其意外修改
print(averager(10))
print(averager(20))
print(averager(30))
print(averager(40))
