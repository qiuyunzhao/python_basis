import matplotlib.pyplot as plt


def pltLine():
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]

    plt.plot(input_values, squares, linewidth=5)  # 设置数据与线宽
    plt.title("Square Numbers", fontsize=24)  # 设置标题
    plt.xlabel("Value", fontsize=14)  # 设置X轴
    plt.ylabel("Square of Value", fontsize=14)  # 设置X轴
    plt.tick_params(axis='both', labelsize=14)  # 设置刻度

    # 打开matplotlib查看器，并显示绘制的图形
    # plt.show()

    # 保存生成的图
    # 第一个实参：存储文件名和格式，文件将存储到py文件所在的路径
    # 第二个实参：将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空白区域，#可省略这个实参。
    plt.savefig('squares_plot.png', bbox_inches='tight')


if __name__ == '__main__':
    pltLine()
