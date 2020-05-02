import matplotlib.pyplot as plt


# 绘制少量数据
def pltScatter():
    # plt.scatter(2, 4, s=200)  # s 指定点的大小

    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    plt.scatter(x_values, y_values, s=100)

    plt.title("Square Numbers", fontsize=24)  # 设置标题
    plt.xlabel("Value", fontsize=14)  # 设置X轴
    plt.ylabel("Square of Value", fontsize=14)  # 设置X轴
    plt.tick_params(axis='both', which='major', labelsize=14)  # 设置刻度标记的大小

    plt.show()


# 绘制大量数据
def pltMassScatter():
    x_values = list(range(1, 1001))
    y_values = [x ** 2 for x in x_values]

    # c: 数据点颜色
    # edgecolor: 去除数据点轮廓
    # s: 数据点大小
    plt.scatter(x_values, y_values, c='red', edgecolor='none', s=6)

    plt.axis([0, 1100, 0, 1100000])  # 设置每个坐标轴的取值范围

    plt.show()


# 颜色映射，凸显数据
# 将参数c设置成了一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射
# http://matplotlib.org/
def pltColormapScatter():
    x_values = list(range(1, 1000))
    y_values = [x ** 2 for x in x_values]

    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

    plt.show()



if __name__ == '__main__':
    # pltScatter()
    # pltMassScatter()
    pltColormapScatter()
