from typing import Any, Dict
from urllib.parse import urlparse

import requests
import json
from define import Hero, Gear

CORE_HERO = ['马超', '吕布',]

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

    ]
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


def resolve_hero_team(valid_teams, invalid_teams):
    """
    ([['马超', '张辽', '曹操'], ['马超', '魏延', '曹操'], ['公孙瓒', '马超', '张辽']], [(['曹纯', '马超', '张辽'], '曹纯')])
    :param valid_teams:
    :param invalid_teams:
    :return:
    """
    if (len(valid_teams) == 0) and (len(invalid_teams) == 0):
        return None

    if len(valid_teams) != 0:
        for team in valid_teams:
            print(f'此账号可以组: {team}')

    if len(invalid_teams) != 0:
        for team in invalid_teams:
            print(f'{team[0]} 缺少武将: {team[1]}')


def ma_chao(hero_list):
    ma_chao_teams = [
        ['马超', '张辽', '曹操'],
        ['马超', '魏延', '曹操'],
        ['公孙瓒', '马超', '张辽'],
        ['曹纯', '马超', '张辽']
    ]
    print(hero_list)
    valid_teams = []
    invalid_teams = []
    for team in ma_chao_teams:
        count = sum(hero in hero_list for hero in team)
        if count == 3:
            valid_teams.append(team)
        elif count == 2:
            missing_hero = [hero for hero in team if hero not in hero_list][0]
            invalid_teams.append((team, missing_hero))
    return valid_teams, invalid_teams


def get_detail_hero_list(hero_list):
    """
    :param hero_list: JSON信息
    :return: tuple(普通武将, XP武将, SP武将)
    """
    other_hero_list = []
    xp_hero_list = []
    s2_hero_list = []
    s3_hero_list = []
    for hero in hero_list:
        country_list = ['汉', '魏', '蜀', '吴', '群', '晋']
        hero['country'] = country_list[int(hero['country'])-1]
        if hero['quality'] == 5:
            if hero['season'] == 'SP':
                other_hero_list.append(hero)
            elif hero['season'] == 'XP':
                xp_hero_list.append(hero)
            elif hero['season'] == 'S2':
                s2_hero_list.append(hero)
            elif hero['season'] == 'S3':
                s3_hero_list.append(hero)
            else:
                other_hero_list.append(hero)
    return {
        's2': s2_hero_list,
        's3': s3_hero_list,
        'xp': xp_hero_list,
        'other': other_hero_list
    }


# 账号武将信息
def request_account_information(url):
    ordersn = get_account_ordersn(url)
    data = {
        'ordersn': ordersn,
        'serverid': 1
    }
    response = requests.post('https://stzb.cbg.163.com/cgi/api/get_equip_detail', data=data)
    account_total = json.loads(response.text)['equip']
    account_information = json.loads(account_total['equip_desc'])
    del account_total['equip_desc']
    skin_info = account_information['dynamic_icon']
    del account_information['dynamic_icon']
    skill_info = account_information['skill']
    del account_information['skill']
    gear_info = account_information['gear']
    del account_information['gear']
    hero_list = account_information['card']
    del account_information['card']
    return account_total, hero_list, skin_info, skill_info, gear_info

def get_account_information(account_total):
    """
        'area_name': '征服赛季',
        'server_name': 'X3999 百业争鸣',
        'status_desc': '上架中',
        'price': 38800,
        'desc_sumup_short': '50张五星武将卡 106个战法 22个宝物',
        'collect_num': 9,
        'highlights': ['2个绝版武将'],
    """
    info = {
        'area_name': account_total['area_name'],
        'server_name': account_total['server_name'],
        'status_desc': account_total['status_desc'],
        'price': account_total['price'],
        'desc_sumup_short': account_total['desc_sumup_short'],
        'collect_num': account_total['collect_num'],
        'highlights': account_total['highlights']
    }
    return info
