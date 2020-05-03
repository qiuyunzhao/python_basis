import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 请求GitHub数据
URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
repo_dicts = response_dict['items']
print("获取到的仓库数量:", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],  # 评星
        'label': repo_dict['description'],  # 描述
        'xlink': repo_dict['html_url'],  # 单击连接
    }
    plot_dicts.append(plot_dict)

# pygal可视化
my_style = LS('#333366', base_style=LCS)  # 设置基色 和 加亮显示的主题

# 自定义图标配置项
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)  # 添加字典实现自定义提示
chart.render_to_file('python_repos.svg')

print("---------finished---------")
