# os 模块让我们可以对操作系统进行访问
import os
import pprint

# os.environ
# 通过这个属性可以获取到系统的环境变量
pprint.pprint(os.environ['path'])

# os.system()
# 可以用来执行操作系统的命令
os.system('dir')
os.system('notepad')
