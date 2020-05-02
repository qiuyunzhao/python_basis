import json
import pygal
from pygal.style import LightColorizedStyle, RotateStyle

from t_下载数据.t3_pouplation_map.country_codes import get_country_code

# 获取指定要求的数据

filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)  # 将数据加载到一个列表中

# 创建一个包含国家编号和人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']  # 国家名称
        population = int(float(pop_dict['Value']))  # 国家人口
        code = get_country_code(country_name)  # 获取pygal中对应的国家编号
        if code:
            cc_populations[code] = population

# 为了用颜色突出人口差别，根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}

for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# 绘制地图
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)  # 设置基色,加量颜色
wm = pygal.maps.world.World(style=wm_style)

wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
