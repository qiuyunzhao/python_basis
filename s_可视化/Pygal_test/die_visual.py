import pygal
from s_可视化.Pygal_test.die import Die


def visual_die():
    # 创建一个骰子
    die = Die()

    # 掷几次骰子，并将结果存储在一个列表中
    results = []

    for roll_num in range(1000):
        result = die.roll()
        results.append(result)

    # 分析结果
    frequencies = []

    # 统计没个点数出现的次数
    for value in range(1, die.num_sides + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # 利用Pygal对结果进行可视化
    hist = pygal.Bar()

    hist.title = "Results of rolling one D6 1000 times."
    hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    hist.add('D6', frequencies)
    hist.render_to_file('die_visual.svg')


if __name__ == '__main__':
    visual_die()
