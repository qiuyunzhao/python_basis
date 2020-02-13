# filter() 从序列中过滤出符合条件的元素，保存到一个新的序列中
#   参数：
#     1.函数，根据该函数来过滤序列（可迭代的结构）
#     2.需要过滤的序列（可迭代的结构）
#   返回值：
#     过滤后的新序列（可迭代的结构）

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 创建一个列表


# 检查一个数字是否是偶数（制定规则的函数）
def get_odd(i):
    if i % 2 == 0:
        return True
    return False


result = filter(get_odd, l)
print(list(result))

# map() 函数
#     可以对可迭代对象中的所有元素做指定的操作，然后将其添加到一个新的对象中返回
#   参数：
#     1.函数，根据该函数来做指定的操作
#     2.需要操作的序列
#   返回值：
#     操作后的新序列
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = map(lambda i: i ** 2, l)
print(list(result))

# sort() 函数
#     用来对 '列表' 中的元素进行排序
#     sort()方法默认是直接比较列表中的元素的大小
#     sorted()排序会影响原来的对象
#     在sort()可以接收一个关键字参数 key
#       key需要一个函数作为参数
#       设置函数作为参数，每次会以列表中的一个元素作为参数来调用函数，并且使用函数的返回值来比较元素的大小进行排序

l = ['bb', 'aaaa', 'c', 'ddddddddd', 'fff']
l.sort(key=len)  # len()返回序列的长度
print('sort -- ', l)

l = [2, 5, '1', 3, '6', '4']
l.sort(key=int)
print('sort -- ', l)

# sorted() 函数
#   与sort()的用法基本一致，但sorted()可以对 '任意的序列' 进行排序
#   使用sorted()排序不会影响原来的对象，而是返回一个新对象
l = (2, 5, '1', 3, '6', '4')
print('sorted()排序前:', l)
print('sorted()排序后:', sorted(l, key=int))
print(l)
