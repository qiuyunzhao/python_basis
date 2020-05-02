import csv
from matplotlib import pyplot as plt
from datetime import datetime

from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

filename = "sitka_weather_2014.csv"

with open(filename) as f:  # 打开文件，将结果文件对象存储在f中
    reader = csv.reader(f)  # 创建一个与该文件相关联的阅读器对象
    header_row = next(reader)  # 读取一行

    # 展示表头信息及其索引
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 从文件中获取日期和最高气温
    dates, highs, lows = [], [], []
    for row in reader:
        # 日期
        current_date = datetime.strptime(row[0], "%Y-%m-%d")  # 格式化日期
        dates.append(current_date)
        # 最高温度
        high = int(row[1])  # 将字符串转换为数字
        highs.append(high)
        # 最低温度
        low = int(row[3])
        lows.append(low)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    # 绘制曲线
    # plt.plot(dates, highs, c='red')
    # plt.plot(dates, lows, c='blue')
    # 绘制曲线并填充颜色
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  # 设置填充

    fig.autofmt_xdate()  # 绘制斜的日期标签，以免它们彼此重叠

    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
