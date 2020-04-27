class A:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class B:
    def __init__(self, name):
        self._name = name

    def __len__(self):
        return 10

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


a = A('孙悟空')
b = B('猪八戒')


# 只要对象中含有name属性，该对象就可以作为参数传递，该函数并不会考虑对象的类型，“ 只要有name属性即可 ”
def say_hello(obj):
    print('say_hello %s' % obj.name)


say_hello(a)
say_hello(b)


# 该函数类型检查，只有obj是A类型的对象时，才可以正常使用，
# 该函数就违反了多态，只适用于一种类型的对象，无法处理其他类型对象，这样导致函数的适应性非常的差
# 注意，向isinstance()这种函数，在开发中一般是不会使用的！
def say_hello_2(obj):
    # 做类型检查
    if isinstance(obj, A):
        print('say_hello_2 %s' % obj.name)


say_hello_2(a)
say_hello_2(b)

# ========================================  应用 ===========================================
# len()
#     之所以一个对象能通过len()来获取长度，是因为对象中具有一个特殊方法__len__
#     换句话说，只要对象中具有__len__特殊方法，就可以通过len()来获取它的长度
l = [1, 2, 3]
s = 'r_单元测试'

print(len(l))
print(len(s))

# print(len(a))  # TypeError: object of type 'r_单元测试' has no len()
print(len(b))
