import os
from pprint import pprint

file_path = 'D:\PycharmProjects\python_basis\16_文件操作'

# os.listdir() 获取指定目录的目录结构
#     需要一个路径作为参数，默认路径为 "." 当前目录
#     返回一个列表，目录中的每一个文件（夹）的名字都是列表中的一个元素
r = os.listdir(file_path)
pprint(r)

# os.getcwd() 获取当前所在的目录
r = os.getcwd()
pprint(r)

# os.chdir() 切换当前所在的目录 作用相当于 cd
os.chdir('D:/PycharmProjects/python_basis/q_文件操作/file')
r = os.getcwd()
pprint(r)

# s.mkdir()  在当前目录下创建一个目录,已存在报错
os.mkdir("aaa")

# os.rmdir()  删除目录，,不存在报错
os.rmdir('aaa')

# os.remove()  删除文件
open('aa.txt', 'w')
os.remove('aa.txt')

# os.rename('旧名字','新名字') 相同路径下文件进行重命名，不同路径下用来移动一个文件
os.rename('aa.txt', 'bb.txt')
os.rename('bb.txt', 'c:/users/lilichao/desktop/bb.txt')
