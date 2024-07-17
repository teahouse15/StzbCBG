from typing import Any, Dict
from urllib.parse import urlparse

import requests
import json

from define import Hero, Gear

main_team = {
    '马超': [
        ['马超', '张辽', '曹操'],
        ['马超', '魏延', '曹操'],
        ['公孙瓒', '马超', '张辽'],
        ['曹纯', '马超', '张辽']
    ],
    '吕布': [
        ['吕布', '貂蝉', '张机'],
        ['吕布', '张机', '孙权'],
        ['吕布', '张机', '魏延'],
        ['吕布', '吕蒙', '田丰']
    ],
    '大乔': [

    ],
    '杜预': [

    ],
    '荀彧': [

    ],
    '马岱': [

    ],
    '关羽': [

    ],
    '华雄': [

    ],

}
start_team = (

)







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
    url = 'https://stzb.cbg.163.com/cgi/mweb/equip/1/202406291702116-1-WTWOLCJRCESBAO?view_loc=equip_list%7Ctag_key%3A%7B%22is_from_ad_reco%22%3A%200,%20%22tag%22%3A%20%22general_rec_din_tfs%22%7D&reco_request_id=17212101443301x1j6&tag=general_rec_din_tfs'
    ordersn = get_account_ordersn(url)
    data = {
        'ordersn': ordersn,
        'serverid': 1
    }
    response = requests.post('https://stzb.cbg.163.com/cgi/api/get_equip_detail', data=data)
    account_total = json.loads(response.text)['equip']
    account_hero_information = json.loads(account_total['equip_desc'])

    hero_list = account_hero_information['card']
    for hero_list in get_hero_list(hero_list):
        print(hero_list)


def get_hero_list(hero_list):
    """
    :param hero_list: JSON信息
    :return: tuple(普通武将, XP武将, SP武将)
    """
    nu_hero_list = []
    xp_hero_list = []
    sp_hero_list = []
    s2_hero_list = []
    s3_hero_list = []
    for hero in hero_list:
        if hero['quality'] == 5:
            if hero['season'] == 'SP':
                sp_hero_list.append(hero['name'])
            elif hero['season'] == 'XP':
                xp_hero_list.append(hero['name'])
            elif hero['season'] == 'S2':
                s2_hero_list.append(hero['name'])
            elif hero['season'] == 'S3':
                s3_hero_list.append(hero['name'])
            else:
                nu_hero_list.append(hero['name'])
    return s2_hero_list, s3_hero_list, xp_hero_list, sp_hero_list, nu_hero_list


def team_check(hero):


    core_heao = ['马超', '']





if __name__ == '__main__':
    test()
