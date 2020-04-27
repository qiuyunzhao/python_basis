# 高阶函数
# 接收函数作为参数，或者将函数作为返回值的函数是高阶函数
# 使用函数作为参数时，实际上是将指定的代码传递进了目标函数


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 创建一个列表


# 检查一个数字是否是偶数
def get_odd(i):
    if i % 2 == 0:
        return True

    return False


# 检查一个数字是否是偶数
def get_big(i):
    if i > 5:
        return True
    return False


def fn(func1, func2, lst):
    odd_list = []
    big_list = []

    # 对列表进行筛选
    for n in lst:
        # 判断n的奇偶
        if func1(n):
            odd_list.append(n)
        if func2(n):
            big_list.append(n)

    # 返回新列表
    return odd_list, big_list


print(fn(get_odd, get_big, l))

# ============================================ 高阶函数的应用 =====================================================

# filter() 从序列中过滤出符合条件的元素，保存到一个新的序列中
#   参数：
#     1.函数，根据该函数来过滤序列（可迭代的结构）
#     2.需要过滤的序列（可迭代的结构）
#   返回值：
#     过滤后的新序列（可迭代的结构）
result = filter(get_odd, l)
print(result)
print(list(result))
