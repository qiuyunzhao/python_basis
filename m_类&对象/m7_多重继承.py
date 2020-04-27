class A(object):
    def test(self):
        print('r_单元测试-test')


class B(object):
    def test(self):
        print('B-test')

    def test2(self):
        print('B-test2')


# 在类名的()后边添加多个类，来实现多重继承
#   多重继承，会使子类同时拥有多个父类，并且会获取到所有父类中的方法和属性
#   在开发中没有特殊的情况，应该尽量避免使用多重继承，因为多重继承会让我们的代码过于复杂
#   如果多个父类中有同名的方法，则会先在第一个父类中寻找，然后找第二个，然后找第三个......(前边父类的方法会覆盖后边父类的方法)
#

class C(A, B):
    pass


c = C()
c.test()
c.test2()

# 类名.__bases__ 这个属性可以用来获取当前类的所有父类
print(B.__bases__)  # (<class 'object'>,)
print(C.__bases__)  # (<class '__main__.r_单元测试'>, <class '__main__.B'>)
