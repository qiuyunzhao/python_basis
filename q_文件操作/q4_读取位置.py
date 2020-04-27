file_name = 'file/demo02.txt'

with open(file_name, 'rb') as file_obj:
    # tell() 方法用来查看当前读取的位置
    print('当前读取到了 -->', file_obj.tell())

    print(file_obj.read(47))

    # seek() 可以修改当前读取的位置，需要两个参数
    #   第一个参数 是要切换到的位置
    #   第二个参数 计算位置方式
    #       可选值：
    #           0 从头计算（默认值）
    #           1 从当前位置计算      需要二进制格式读才支持
    #           2 从最后位置开始计算   需要二进制格式读才支持

    file_obj.seek(49)
    print('当前读取到了 -->', file_obj.tell())
    print(file_obj.read(81))

    file_obj.seek(49, 0)
    print('当前读取到了 -->', file_obj.tell())
    print(file_obj.read(81))

    print('当前读取到了 -->', file_obj.tell())
    file_obj.seek(69, 1)
    print('当前读取到了 -->', file_obj.tell())
    print(file_obj.read(57))

    file_obj.seek(-10, 2)
    print('当前读取到了 -->', file_obj.tell())
    print(file_obj.read(10))

