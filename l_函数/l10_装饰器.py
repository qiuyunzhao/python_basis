def add(a, b):
    print('执行add')
    result = a + b
    return result


def mul(a=1, b=2):
    print('执行mul')
    result = a * b
    return result


def say_hello():
    print('执行say_hello')


# 希望函数可以在计算前、计算结束后做一些处理
# 可以直接通过修改函数中的代码来完成这个需求，但是会产生以下一些问题
#   ① 如果要修改的函数过多，修改起来会比较麻烦
#   ② 并且不方便后期的维护
#   ③ 并且这样做会违反开闭原则（OCP）

def new_add(a, b):
    print('计算开始~~~')
    a *= 10
    b *= 10

    result = add(a, b)  # 调用被装饰的函数

    print('计算结束~~~')
    return result


r = new_add(1, 2)
print(r)

# 上边的方式，已经可以在不修改源代码的情况下对函数进行扩展了
# 但是，这种方式要求我们每扩展一个函数就要手动创建一个新的函数，实在是太麻烦了,维护困难
# 为了解决这个问题，我们创建一个函数，让这个函数可以自动的帮助我们生产函数
print('--------------------------------装饰器-------------------------------')


# 装饰器1
def decorator_func1(old):
    """
        参数：
            old 要扩展的函数对象
    """

    # 创建一个新函数
    def new_function(*args, **kwargs):
        print('decorator_func1 开始执行~~~~')

        result = old(*args, **kwargs)  # 调用被装饰的函数

        print('decorator_func1 执行结束~~~~')
        return result

    # 返回新函数
    return new_function


decorator_func1(say_hello)()
print(decorator_func1(add)(1, 2))
print(decorator_func1(mul)(b=10, a=20))


# 装饰器2
def decorator_func2(old):
    """
        参数：
            old 要扩展的函数对象
    """

    def new_function(*args, **kwargs):
        print('decorator_func2 开始执行~~~~')

        result = old(*args, **kwargs)  # 调用被装饰的函数

        print('decorator_func2 执行结束~~~~')
        return result

    return new_function


# decorator_func1()这种函数我们就称为装饰器。通过装饰器，可以在不修改原来函数的情况下来对函数进行扩展
# 定义函数时，可以通过@装饰器，使用指定的装饰器来装饰当前的函数
# 可以同时为一个函数指定多个装饰器，这样函数将会按照从内向外的顺序被装饰
print('--------------------------------装饰器使用-------------------------------')


@decorator_func1
@decorator_func2
def my_hello():
    print('大家好~~~')


my_hello()
