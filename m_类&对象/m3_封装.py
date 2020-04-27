print('=========================== 方式1：隐藏属性名称、get set 方法 ===========================')


# 将属性重命名 ，无法通过 "对象.属性名" 访问
# 可通过 "对象.属性重命名" 访问

class Dog:

    def __init__(self, name, age):
        self.hidden_name = name
        self.hidden_age = age

    def set_name(self, name):
        self.hidden_name = name

    def get_name(self):
        return self.hidden_name

    def set_age(self, age):
        if age > 0:
            self.hidden_age = age

    def get_age(self):
        return self.hidden_age

    def say_hello(self):
        print('大家好，我是 %s' % self.hidden_name)


d = Dog('旺财', 8)
d.set_name('小黑')
d.set_age(-10)
print(d.get_name(), '--', d.get_age())


# 并不是完全隐藏属性 下边方法依然可以访问
# d.hidden_age = -10
# print(d.get_age())

# ====================================== 实际生产中常用 ======================================

#   重命名写法太麻烦且不易记，一般会将一些私有属性以 “_” 开头
#   一般情况下，使用 “_” 开头的属性都是私有属性，没有特殊需要不要修改私有属性
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


p = Person('孙悟空')

print(p._name)  # 可以访问，但约定俗成不去这样访问

print('=========================== 方式2：属性使用双下划线开头、get set 方法 （不用）===========================')


# "__xxx", 双下划线开头的属性，是对象的隐藏属性，隐藏属性只能在类的内部访问，无法通过 "对象.__xxx" 访问
# 这种方式隐藏属性只不过是Python自动将属性改名 "_类名__属性名"，可通过"对象._类名__xxx" 访问

class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def get_area(self):
        return self.__width * self.__height


rec = Rectangle(5, 10)
print('width:', rec.get_width(), ' height:', rec.get_height())
print('area', rec.get_area())

# 无法通过 "对象.__xxx" 访问
# print(rec.__width)  # AttributeError: 'Rectangle' object has no attribute '__width'

# 并不是完全隐藏属性 下边方法依然可以访问
print(rec._Rectangle__width)

print('=========================== 方式2：属性使用双下划线开头、get set 方法 （不用）===========================')
