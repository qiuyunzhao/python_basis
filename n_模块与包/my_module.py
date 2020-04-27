# 模块中定义的变量，可以通过引入模块访问到
a = 1
b = 2

# _的变量，只能在模块内部访问，在通过import * 引入时，不会引入_开头的变量
_c = 30


# 模块中定义函数，可以通过引入模块访问到
def test():
    print('my_module test()')


def test2():
    print('my_module test2()')


# 模块中定义类
class Person:
    def __init__(self):
        self.name = 'my_module 孙悟空'

    def say_hello(self):
        print('r_单元测试 ', self.name)


# 测试代码，这部分代码，只要当当前文件作为主模块的时候才需要执行
#   而当模块被其他模块引入时，不需要执行的，此时我们就必须要检查当前模块是否是主模块
if __name__ == '__main__':
    test()
    p = Person()
    print(p.name)
