import matplotlib.pyplot as plt
from s_可视化.matplotlib_test.random_walk import RandomWalk


def draw_trace():
    while True:
        # 创建一个RandomWalk实例，并将其包含的点都绘制出来
        rw = RandomWalk()
        rw.fill_walk()

        # 设置绘图窗口的尺寸
        plt.figure(figsize=(10, 6))

        # 突出路径，后绘制的颜色更深
        # 参数：
        #   c:颜色
        #   cmap:颜色映射
        #   edgecolor:去除点的边框
        #   s:点的大小
        point_numbers = list(range(rw.num_points))
        plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=5)

        # 突出起点和终点
        plt.scatter(0, 0, c='green', edgecolors='none', s=100)  # 起点
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  # 终点

        # 隐藏坐标轴
        plt.xticks([])
        plt.yticks([])
        plt.show()

        keep_running = input("重新绘制吗? (y/n): ")
        if keep_running == 'n':
            break


if __name__ == '__main__':
    draw_trace()
