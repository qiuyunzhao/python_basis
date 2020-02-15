class Animal:
    def run(self):
        print('动物会跑~~~')

    def sleep(self):
        print('动物睡觉~~~')


#  - 通过继承可以直接让子类获取到父类的方法或属性
#  - 在创建类时，如果省略了父类，则默认父类为object object是所有类的父类，所有类都继承自object
#       class Person(object):
#          pass

class Dog(Animal):

    # 方法重写
    def run(self):
        print('狗跑~~~~')

    def bark(self):
        print('汪汪汪~~~')


d = Dog()

d.run()
d.sleep()
d.bark()

# isinstance()用来检查一个对象是否是一个类的实例
print(isinstance(d, Dog))
print(isinstance(d, Animal))
print(isinstance(print, object))

# issubclass() 检查一个类是否是另一个类的子类
print(issubclass(Dog, Animal))
print(issubclass(Animal, object))
print(issubclass(Dog, object))
