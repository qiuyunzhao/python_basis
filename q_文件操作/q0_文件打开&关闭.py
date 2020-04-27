# open(file, mode='r_单元测试', buffering=-1, encoding_=None, errors=None, newline=None, closefd=True, opener=None)
# 参数：
#   file 要打开的文件的名字（路径）
# 返回值：
#   返回一个对象，这个对象就代表了当前打开的文件

# 在windows系统使用路径时，
# 可以使用 / 来代替 \
# 可以使用 \\ 来代替 \
# 可以使用原始字符串
file_path = 'file/demo.txt'
file_path = 'file\\demo.txt'
file_path = r_单元测试'file\demo.txt'

# 使用..来返回一级目录(当前目录是16_文件操作)
file_path = '../README.md'

# 使用绝对路径
file_path = r_单元测试'D:\PycharmProjects\python_basis\16_文件操作\file\demo.txt'

file_obj = open(file_path)  # 打开 file_name 对应的文件
print(file_obj)

# close()方法来关闭文件
file_obj.close()

# ============================== 生产中使用如下 ==================================
# with ... as 语句

# with open(file_name) as file_obj :
#     在with语句模块中可以直接使用file_obj来做文件操作
#     此时这个文件只能在with中使用，一旦with结束则文件会自动close()

file_name = 'file/demo.txt'

try:
    with open(file_name) as file_obj:
        print(file_obj.read())
except FileNotFoundError:
    print(f'{file_name} 文件不存在')
