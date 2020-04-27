try:
    # try中放置可能出现错误的代码
    print(10 / 0)
except:
    # except中放置出错以后的处理方法
    print('except,出错了')
else:
    print('else,正常')
finally:
    print('finally,总会执行')

print('------------------------- 程序执行结束 -------------------------')
