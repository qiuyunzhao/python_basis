class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 装饰器，用来将一个set或get方法，转换为对象的属性
    #   - set或get 方法添加装饰器以后，我们就可以像调用属性一样使用 set或get 方法
    #   - 使用装饰器的 set get 方法，必须和属性名是一样的
    #   - 必须有 @property 才能有 @属性名.setter

    # getter方法的装饰器：@property
    @property
    def name(self):
        print('getter方法调用了')
        return self._name

    # setter方法的装饰器：@属性名.setter
    @name.setter
    def name(self, name):
        print('setter方法调用了')
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


p = Person('猪八戒', 18)

p.name = '孙悟空'
p.age = 28

print(p.name, p.age)
