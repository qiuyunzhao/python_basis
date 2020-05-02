import pygal

# 创建地图实例
wm = pygal.maps.world.World()

# 设置标题
wm.title = 'North, Central, and South America'

# add()方法，接受一个标签和一个列表，其中后者包含我们要突出的国家的国别码。
# 每次调用add()都将选择一种新颜色，并在图表左边显示该颜色和指定的标签。

# 将不同区域的国家用不同颜色标注
# wm.add('North America', ['ca', 'mx', 'us'])
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

# 在世界地图上呈现数字数据
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

# 方法render_to_file()创建一个包含该图表的.svg文件
wm.render_to_file('americas.svg')
