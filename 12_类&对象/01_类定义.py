# ============================================== 类 =============================================
class Person:
    # 类中定义的变量为公共属性，所有该类实例都可以访问
    name = 'swk'

    # - 类中定义的方法为公共方法，所有该类实例都可以访问
    # - 方法每次被调用时，解析器都会自动传递第一个实参
    #       第一个参数，就是调用方法的对象本身，一般我们都会将这个参数命名为self
    #           如果是p1调的，则第一个参数就是p1对象
    #           如果是p2调的，则第一个参数就是p2对象
    def say_hello(self):
        print('你好！ %s' % self.name)  # 在方法中不能直接访问类中的属性

    def eat(self, food):
        print(self.name, "吃", food)


# ============================================== 对象 =============================================

# 创建Person的实例
p1 = Person()
p2 = Person()

print("---------------------------类公共属性")
print(p1.name)  # swk
print(p2.name)  # swk

print("---------------------------类公共方法")
# 函数调用，传几个参数，就有几个实参;
# 方法调用，默认传递第一个参数是调用方法的对象本身
p1.say_hello()  # 你好！ swk
p2.say_hello()  # 你好！ swk

p1.eat('馒头')

print("---------------------------创建对象自己的属性")

# - 类对象和实例对象中都可以单独保存属性（方法）
#     - 如果这个属性（方法）是所有的实例共享的，则应该将其保存到类对象中
#     - 如果这个属性（方法）是某个实例独有，则应该保存到实例对象中

# - 属性和方法查找的流程
#     当我们调用一个对象的属性时，解析器会先在当前对象中寻找是否含有该属性，
#         如果有，则直接返回当前的对象的属性值，
#         如果没有，则去当前对象的类对象中去寻找，如果有则返回类对象的属性值，
#         如果类对象中依然没有，则报错！

p1.name = '猪八戒'
p2.name = '沙和尚'

print(p1.name)  # 猪八戒
print(p2.name)  # 沙和尚

p1.say_hello()  # 你好！ 猪八戒
p2.say_hello()  # 你好！ 沙和尚

print("---------------------------删除对象自己的属性")
del p1.name  # 删除p1的name属性

print(p1.name)  # swk
print(p2.name)  # 沙和尚
