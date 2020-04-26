import json

numbers = [2, 3, 5, 7, 11, 13]

file_name = 'file/numbers.json'

# 写入
try:
    with open(file_name, 'a') as f_obj:
        json.dump(numbers, f_obj)
except FileNotFoundError:
    print(f'{file_name} 文件不存在')
else:
    print('写入成功')

# 读取
try:
    with open(file_name) as f_obj:
        result = json.load(f_obj)
except FileNotFoundError:
    print(f'{file_name} 文件不存在')
else:
    print('读取成功：', result)
