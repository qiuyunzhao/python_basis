from random import choice


class RandomWalk():
    """" 生成随机漫步数据的属性 """

    def __init__(self, num_points=10000):
        """初始化随机漫步的属性"""
        # 走多少步
        self.num_points = num_points
        # 足迹列表，所有的漫步都起始于（0,0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """"计算随机漫步所要经过的所有点"""
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])  # 决定前进方向
            x_distance = choice([0, 1, 2, 3, 4])  # 前进的距离
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])  # 决定前进方向
            y_distance = choice([0, 1, 2, 3, 4])  # 前进的距离
            y_step = y_direction * y_distance

            # 禁止原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # 将下一步坐标加入足迹列表
            self.x_values.append(next_x)
            self.y_values.append(next_y)
