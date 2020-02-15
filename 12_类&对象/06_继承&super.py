class Animal:

    def __init__(self, name):
        self._name = name

    def run(self):
        print('动物会跑~~~')

    def sleep(self):
        print('动物睡觉~~~')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


# 父类中的所有方法都会被子类继承，包括特殊方法，也可以重写特殊方法
class Dog(Animal):

    # 重写特殊方法
    def __init__(self, name, age):
        # 调用父类的__init__来初始化父类中定义的属性
        # super() 可以用来获取当前类的父类，通过super()返回对象调用父类方法时，不需要传递self
        super().__init__(name)
        self._age = age

    # 重写方法
    def run(self):
        print('狗跑~~~~')

    # 扩展方法
    def bark(self):
        print('汪汪汪~~~')

    # 扩展属性
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


d = Dog('旺财', 18)

print(d.name)  # 继承自父类的
print(d.age)  # 子类扩展的
