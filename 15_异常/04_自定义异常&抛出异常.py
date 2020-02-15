# 自定义异常类：创建一个类继承Exception即可
class MyError(Exception):
    pass


# 抛出异常的目的，告诉调用者这里调用时出现问题，希望你自己处理一下
# raise用于向外部抛出异常，后边可以跟一个异常类，或异常类的实例

def add_exception(a, b):
    # 如果a和b中有负数，抛出异常
    if a < 0 or b < 0:
        # raise Exception
        # raise Exception('两个参数中不能有负数！')
        raise MyError('自定义的异常')
    r = a + b
    return r
    # 也可以通过if else来代替异常的处理,但是if处理的情况需是已知的


print(add_exception(-123, 456))
