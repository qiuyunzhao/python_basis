#  类中可以定义特殊方法，特殊方法都是以 “__” 开头， “__” 结尾
#  特殊方法可以调用，但不要尝试去调用特殊方法，特殊方法将会在特殊的时刻自动调用

# 创建对象的流程 p1 = Person()的运行流程
#   1.创建一个变量
#   2.在内存中创建一个新对象
#   3.__init__(self)方法执行
#   4.将对象的id赋值给变量


class Dog:
    print('Person类中代码块先被执行，且只执行一次')

    # 公共的属性...

    # 初始化方法
    #     init会在对象创建以后立即执行，用来向新创建的对象中初始化属性
    #     调用类创建对象时，类后边的所有参数都会依次传递到init()中
    def __init__(self, name, age, gender, host):
        self.name = name  # 通过self向新建的对象中初始化属性
        self.age = age
        self.gender = gender
        self.host = host

    # 其他的方法
    def sleep(self):
        print('%s 休息中~~' % self.name)

    def watchDoor(self):
        print('%s 在看门~~' % self.name)


d = Dog('哮天犬', 500, 'male', '二郎神')
d.sleep()
d.watchDoor()

# 目前可以通过 “对象.属性” 来修改属性的值，导致对象中的属性可以随意修改，非常的不安全
d.age = -10
print(d.age)

# 现在我们就需要一种方式来增强数据的安全性
#   1.属性不能随意修改
#   2.属性不能修改为任意的值
