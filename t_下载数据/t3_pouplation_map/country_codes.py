# population_data.json中包含的是三个字母的国别码，但Pygal使用两个字母的国别码。
# 需要根据国家名获取两个字母的国别码。

from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """根据指定的国家，返回 Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():  # 遍历COUNTRIES字典
        if name == country_name:
            return code

    # 如果没有找到指定的国家，就返回None
    return None


if __name__ == '__main__':
    print(get_country_code('Andorra'))
    print(get_country_code('United Arab Emirates'))
    print(get_country_code('Afghanistan'))
