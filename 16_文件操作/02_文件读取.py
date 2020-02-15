import pprint

file_name = 'file/demo.txt'

try:
    # 调用open()来打开一个文件，可以将文件分成两种类型
    #     -纯文本文件（使用utf-8等编码编写的文本文件）
    #     -二进制文件（图片、mp3、ppt等这些文件）
    # open()打开文件时，默认是以文本文件的形式打开的，但是open()默认的编码为None。处理文本文件时，必须要指定文件的编码
    with open(file_name, encoding='utf-8') as file_obj:
        # read() 来读取文件中的内容
        #     直接调用read()，会将文本文件的所有内容全部都读取出来，
        #     如果要读取的文件较大的话，会一次性将文件的内容加载到内存中，容易导致内存泄漏，
        #     所以对于较大的文件，不要直接调用read()

        # read(size) size作为参数，参数用来指定要读取的字符的数量
        #     默认值为-1，它会读取文件中的所有字符
        #     为size指定一个值，read()会读取指定数量的字符，
        #        每一次读取都是从上次读取到位置开始继续读取，
        #        如果字符的数量小于size，则会读取剩余所有的，
        #        如果已经读取到了文件的最后了，则会返回''空串。

        # readline()
        #     该方法可以用来读取一行内容

        # readlines()
        #     该方法用于一行一行的读取内容，它会一次性将读取到的内容封装到一个列表中返回

        # content = file_obj.read(10)
        # print(content, len(content))

        # content = file_obj.readline()
        # print(content, len(content))

        contents = file_obj.readlines()
        for content in contents:
            pprint.pprint(content)

except FileNotFoundError:
    print(f'{file_name} 这个文件不存在！')

print('----------------------------------- 读取大文件 -----------------------------------')

try:
    with open(file_name, encoding='utf-8') as file_obj:
        file_content = ''  # 定义一个变量，来保存文件的内容
        chunk = 100  # 定义一个变量，来指定每次读取的大小

        # 创建一个循环来读取文件内容
        while True:
            content = file_obj.read(chunk)  # 读取chunk大小的内容
            if not content:  # 检查是否读取到了内容
                break  # 没读取到内容，退出循环

            # 处理内容
            print(content, end='')  # end='' 打印不换行
            file_content += content

except FileNotFoundError:
    print(f'{file_name} 这个文件不存在！')

# print(file_content)
