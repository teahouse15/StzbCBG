from typing import Any, Dict
from urllib.parse import urlparse

import requests
import json

from define import Hero, Gear


def get_account_ordersn(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')
    return path_parts[5]


# 定义一个函数，将 JSON 数据解析为 Hero 类的实例
def parse_hero(json_data: Dict[str, Any]) -> Hero:
    # 提取 gear 数据并将其解析为 Gear 类的实例，如果存在 gear 字段
    gear_data = json_data.pop('gear', None)
    gear = Gear(**gear_data) if gear_data else None
    # 将剩余的 JSON 数据解析为 Hero 类的实例，并将 gear 实例作为参数传入
    return Hero(gear=gear, **json_data)


def test():
    url = 'https://stzb.cbg.163.com/cgi/mweb/equip/1/202406281002116-1-WSVKTHNQ5KWZ9D?view_loc=equip_list%7Ctag_key%3A%7B%22is_from_ad_reco%22%3A%200,%20%22tag%22%3A%20%22general_rec_din_tfs%22%7D&reco_request_id=1721200271025evUgP&tag=general_rec_din_tfs'
    ordersn = get_account_ordersn(url)
    data = {
        'ordersn': ordersn,
        'serverid': 1
    }
    response = requests.post('https://stzb.cbg.163.com/cgi/api/get_equip_detail', data=data)
    account_total = json.loads(response.text)['equip']
    account_hero_information = json.loads(account_total['equip_desc'])

    hero_list = account_hero_information['card']
    print(get_hero_list(hero_list))
    # for hero in hero_list:
    #     # 使用 parse_hero 函数将 JSON 数据解析为 Hero 类的实例
    #     hero = parse_hero(hero)
    #
    #     # 输出 Hero 实例的属性
    #     print(hero.__dict__)


def get_hero_list(hero_list):
    hero_name_list = []
    for hero in hero_list:
        if hero['quality'] == 5:
            hero_name_list.append(hero['name'])
    return hero_name_list


if __name__ == '__main__':
    test()
