file_name = 'file/请坐.jpg'

# 读取模式
#   t 读取文本文件（默认值），读取文本文件时，size是以字符为单位的
#   b 读取二进制文件，读取二进制文件时，size是以字节为单位

with open(file_name, 'rb') as file_obj:  # rb 读二进制
    new_name = 'file/请坐_副本.jpg'  # 定义一个新的文件

    with open(new_name, 'wb') as new_obj:  # wb 写二进制

        chunk = 1024 * 100  # 定义每次读取的大小

        while True:
            content = file_obj.read(chunk)  # 从已有的对象中读取数据

            if not content:
                break  # 内容读取完毕，终止循环

            new_obj.write(content)  # 将读取到的数据写入到新对象中
