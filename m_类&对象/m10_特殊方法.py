# 特殊方法，也称为魔术方法
# 特殊方法都是使用 “__” 开头和结尾的
# 特殊方法一般不需要我们手动调用，需要在一些特殊情况下自动执行


class Person(object):

    # 调用：创建类的实例时调用
    # 作用：创建对象时为属性赋值
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 调用：没有被引用的对象进行垃圾回收时
    # 作用：垃圾、资源回收
    def __del__(self):
        print('r_单元测试()对象被删除了~~~', self)

    # 调用： __str__（）这个特殊方法会在尝试将对象转换为字符串的时候调用
    # 作用： 它的作用可以用来指定对象转换为字符串的结果 （print函数显示结果）
    def __str__(self):
        return 'Person [name=%s , age=%d]' % (self.name, self.age)

    # 调用： __repr__() 这个特殊方法会在对当前对象使用repr()函数时调用
    # 作用： 它的作用是指定对象在 ‘交互模式’ 中直接输出的效果
    def __repr__(self):
        return 'Hello'

    # 调用： __bool__(self) 这个特殊方法会在对当前对象使用bool()函数时调用
    # 作用： 可以通过bool来指定对象转换为布尔值的情况
    def __bool__(self):
        return self.age > 17

    # object.__add__(self, other)
    # object.__sub__(self, other)
    # object.__mul__(self, other)
    # object.__matmul__(self, other)
    # object.__truediv__(self, other)
    # object.__floordiv__(self, other)
    # object.__mod__(self, other)
    # object.__divmod__(self, other)
    # object.__pow__(self, other[, modulo])
    # object.__lshift__(self, other)
    # object.__rshift__(self, other)
    # object.__and__(self, other)
    # object.__xor__(self, other)
    # object.__or__(self, other)

    # __len__()                  获取对象的长度
    # object.__lt__(self, other) 小于 <
    # object.__le__(self, other) 小于等于 <=
    # object.__eq__(self, other) 等于 ==
    # object.__ne__(self, other) 不等于 !=
    # object.__gt__(self, other) 大于 >
    # object.__ge__(self, other) 大于等于 >=

    # 调用： len() 获取对象的长度时
    # 调用： 获取对象长度
    def __len__(self):
        return len(self.name)

    # 调用： __gt__会在对象做大于比较的时候调用，该方法的返回值将会作为比较的结果
    # 调用： 他需要两个参数，一个self表示当前对象，other表示和当前对象比较的对象
    def __gt__(self, other):
        return self.age > other.age


# =========================================================================
p1 = Person('大师兄，孙悟空', 15)
p2 = Person('猪八戒', 28)

# __str__(self) 打印一个对象时，实际上打印的是对象的中特殊方法 __str__()的返回值
print(p1)  # Person [name=孙悟空 , age=18]
print(p2)  # Person [name=猪八戒 , age=28]

# __repr__(self) 打印的是对象的中特殊方法 __repr__()的返回值
print(repr(p1))

# __gt__(self, other)
print(p1 > p2)
print(p2 > p1)

# __len__(self)
print(len(p1))

# __bool__(self)
print(bool(p1))

# __bool__(self)
if p1:
    print(p1.name, '已经成年了')
else:
    print(p1.name, '还未成年了')
