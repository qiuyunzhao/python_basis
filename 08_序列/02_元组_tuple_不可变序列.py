# 元组 tuple
# 元组是一个不可变的序列，它的操作的方式基本上和列表是一致的。在操作元组时，把元组当成是一个不可变的列表就ok了
# 一般当我们希望数据不改变时，就使用元组，其余情况都使用列表

print('----------------------------------------------------------------------------------------------------1.元组创建')
my_tuple = ()  # 创建了一个空元组
print(my_tuple, type(my_tuple))  # () <class 'tuple'>

my_tuple = (1, 2, 3, 4, 5)  # 创建了一个5个元素的元组
print(my_tuple[3])

# my_tuple[3] = 10  # 元组是不可变对象 TypeError: 'tuple' object does not support item assignment

my_tuple = 10, 20, 30, 40  # 当元组不是空元组时，括号可以省略
my_tuple = 40,  # 不加","表示int
print(my_tuple, type(my_tuple))

print('----------------------------------------------------------------------------------------------------2.序列解包')
my_tuple = 10, 20, 30, 40
a, b, c, d = my_tuple  # 元组的解包（解构）,解包指就是将元组当中每一个元素都赋值给一个变量
print('a =', a, 'b =', b, 'c =', c, "d =", d)

# 交互a 和 b的值
a = 100
b = 300
a, b = b, a  # "="右边是元组
print('a=', a, 'b=', b)

# 元组进行解包时，变量的数量必须和元组中的元素的数量一致。可以在变量前边添加*，*变量会获取元组中所有剩余的元素组成列表
# 不能同时出现两个或以上的*变量
# *a, *b, c = my_tuple  # SyntaxError: two starred expressions in assignment

my_tuple = 10, 20, 30, 40
a, b, *c = my_tuple
print('a =', a, 'b =', b, 'c =', c, 'type(c)', type(c))

a, b, *c = [1, 2, 3, 4, 5, 6, 7]
a, *b, c = my_tuple
print('a =', a, 'b =', b, 'c =', c, 'type(b)', type(b))

a, b, *c = 'hello world'
*a, b, c = my_tuple
print('a =', a, 'b =', b, 'c =', c, 'type(a)', type(a))
