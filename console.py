from funcs import *
from define import Hero

url = input("请输入需要解析的网址: ")

# 发请求
response_data = request_account_information(url)
account_total = response_data[0]
account_information = response_data[1]
hero_list = response_data[2]

resolve_hero_team(*ma_chao(hero_list))
# 解析JSON



# 解析武将信息


# 判断武将队伍