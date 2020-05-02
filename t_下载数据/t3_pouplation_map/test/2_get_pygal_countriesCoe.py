from pygal_maps_world.i18n import COUNTRIES

# Pygal使用的国别码存储在模块i18n（ internationalization的缩写）中。
# 字典COUNTRIES包含的键和值分别为两个字母的国别码和国家名。

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
