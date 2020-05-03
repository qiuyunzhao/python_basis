import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# 读取响应状态码
print("Status code:", r.status_code)  # 打印请求状态

# 将API响应结果存储在一个变量中
response_dict = r.json()

# ============================= 处理结果 ====================================
print("仓库总数量:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("获取到的仓库数量:", len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))  # 仓库中有多少项

for key in sorted(repo_dict.keys()):  # 打印每一项的键名
    print(key, ":", repo_dict[key])
