print('------------------------- 异常出现前 -------------------------')
l = []

try:
    # print(c)
    # print(l[10])
    print(10 / 0)
    # 1 + 'hello'
except NameError:
    # 如果except后不跟任何的内容，则它会捕获到所有的异常
    # 如果在except后跟着一个异常的类型，那么此时它只会捕获该类型的异常
    print('出现 NameError 异常')
except IndexError:
    print('出现 IndexError 异常')
except ZeroDivisionError:
    print('出现 ZeroDivisionError 异常')
except Exception as e:
    # Exception 是所有异常类的父类，所以如果except后跟的是Exception，他也会捕获到所有的异常
    # 可以在异常类后边跟着一个 “as xx” 此时 xx 就是异常对象
    print('未知异常', e, type(e))
else:
    print('没有发生异常')
finally:
    print('finally 总会执行')

print('------------------------- 程序执行结束 -------------------------')
