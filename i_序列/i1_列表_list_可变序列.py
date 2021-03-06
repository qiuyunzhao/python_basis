# 列表中可以保存任意的对象
print('---------------------------------------------------------------------------------------0.不可变序列转换成可变序列')
# list() 方法用于将元组或字符串转换为列表。
s = 'r_单元测试 world1'
print(list(s))

print('-----------------------------------------------------------------------------------------------------------1.增')
stus = ['孙悟空']

stus[0:0] = ['唐僧']  # 列表头插入元素
print(stus)

stus.append('沙僧')  # 列表尾插入元素
print(stus)

stus.insert(2, '猪八戒')  # 向列表的指定位置插入一个元素
print(stus)

stus.extend(['狐狸精', '白骨精'])  # 使用新的序列来扩展当前序列
stus += ['牛魔王', '铁扇公主']  # 同上
print(stus)

print('-----------------------------------------------------------------------------------------------------------2.删')
stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '牛魔王', '铁扇公主', '红孩儿', '嫦娥', '玉帝', '如来', '观音']

del stus[2]  # 删除索引为2的元素
print(stus)

del stus[0:2]  # 删除指定范围内的数据 [0,2)
print(stus)
stus[1:3] = []  # 删除指定范围内的数据 [1,3)
print(stus)

# 根据索引删除并返回被删除的元素
result = stus.pop(2)  # 删除索引为2的元素
# result = stus.pop()  # 删除最后一个
print(stus, '  result =', result)

stus.remove('红孩儿')  # 删除指定值得元素(如果相同值得元素有多个，只会删除第一个)
print(stus)

del stus[::2]  # 删除指定步长的数据  0,2,4...
print(stus)

stus.clear()  # 清空序列
print(stus)

print('-----------------------------------------------------------------------------------------------------------3.改')
stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧']

stus[0] = 'SunWuKong'
print(stus)

stus[0:2] = ['牛魔王', '红孩儿', '二郎神']  # 使用新的列表替换旧元素 [0,2)
print(stus)

stus[::2] = ['1', '2', '3']  # 当设置了步长时，序列中元素的个数必须和切片中元素的个数一致  0,2,4...
print(stus)

print('-----------------------------------------------------------------------------------------------------------4.查')
stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精', '沙和尚', '沙和尚']

# 是否存在
print('牛魔王' in stus)
print('牛魔王' not in stus)

# 出现次数
print(stus.count('沙和尚'))

# 第一次出现位置
print(stus.index('沙和尚'))

# 第二个参数，表示查找的起始位置(包含),第三个参数，表示查找的结束位置(不包含)
print(stus.index('沙和尚', 2, 5))

print('---------------------------------------------------------------------------------------------------------5.排序')
lists = list('acbedaagfjihk')

lists.sort()  # 升序排序
print(lists)

lists.sort(reverse=True)  # 降序排序
print(lists)

# 自定义排序规则见 l_函数 的 07_匿名函数

print('---------------------------------------------------------------------------------------------------------6.翻转')
lists.reverse()  # 翻转
print(lists)

print('---------------------------------------------------------------------------------------------------------7.复制')
lists = ['孙悟空', '猪八戒', '沙和尚', '唐僧']
copy_list = lists.copy()
print(lists is copy_list, ' copy_list=', copy_list)

print('---------------------------------------------------------------------------------------------------------8.遍历')

stus = ['唐僧', '孙悟空', '猪八戒', '沙和尚']

i = 0
while i < len(stus):
    print(stus[i])
    i += 1

for s in stus:
    print(s)

print('----------------------------------------------------------------------------------------------------9.range函数')
# range()是一个函数，可以用来生成一个自然数的序列，一般用在 for 循环中
# 该函数需要三个参数
#   1.起始位置（可以省略，默认是0）
#   2.结束位置
#   3.步长（可以省略，默认是1）

r = range(5)  # 生成序列: [0,1,2,3,4]
print(r)
r = range(0, 10, 2)  # [0, 2, 4, 6, 8]
print(list(r))
r = range(10, 0, -1)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list(r))

for i in range(5):
    print(i)
