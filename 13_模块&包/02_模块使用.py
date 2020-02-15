def test2():
    print('主模块 test2()')


print('============================ 引入模块 ============================')
# 语法：
#   import xxx
#   import xxx as yyy

import my_module as m

print(m.a, m.b)  # 访问模块中的变量：模块名.变量名

m.test()  # 访问模块中的函数：模块名.函数

p = m.Person()  # 访问模块中的类：模块名.类
print(p.name)
p.say_hello()

print('============================ 引入模块中的部分内容 ============================')
# 语法：
#   from 模块名 import 类,变量,函数....
#   from xxx import yyy , zzz , fff

from my_module import Person, test, test2

p1 = Person()  # 引入模块中的类
print(p1)

test()  # 引入模块中的函数

test2()  # 引入模块中的函数 覆盖 本模块的同名函数

print('============================ 为引入的变量和函数使用别名 ============================')
# 语法：
#   from 模块名 import 变量 as 别名
#   from xxx import yyy as zz

from my_module import test2 as new_test2

test2()
new_test2()

print('============================ import * 全部引入 ============================')
# 语法：
#   from xxx import *      引入到模块中所有内容，一般不会使用
#   注意是否会覆盖本模块中同名内容
from my_module import *

print(a)

test2()

p1 = Person()
print(p1)
print(p1.name)
