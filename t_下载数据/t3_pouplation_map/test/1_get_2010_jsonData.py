import json

# 获取指定要求的数据

filename = '../population_data.json'

with open(filename) as f:
    pop_data = json.load(f)  # 将数据加载到一个列表中

    # 打印每个国家2010年的人口数量
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            # population = int(pop_dict['Value'])  # 字符串转整数（若数据格式错误有小数会报错）
            population = int(float(pop_dict['Value']))  # 字符串先转浮点数再转整数
            print(country_name + ": " + str(population))
