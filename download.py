import requests
import os
import logging


# 对logger进行配置——日志等级&输出格式
logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] - [%(filename)s]:[%(lineno)d] - [%(levelname)s]"
                                                " - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")

logger = logging.getLogger(__name__)

SKIN_LATEST = 261
HERO_LATEST = 730

SKIN_MEDIUM_PATH = 'res/cards/medium/skin/'
HERO_MEDIUM_PATH = 'res/cards/medium/hero/'

SKIN_WATERMARK_PATH = 'res/cards/watermark/skin/'
HERO_WATERMARK_PATH = 'res/cards/watermark/hero/'

SKIN_MEDIUM_URL = 'https://cbg-stzb.res.netease.com/game_res/cards/cut/card_medium_110'
HERO_MEDIUM_URL = 'https://cbg-stzb.res.netease.com/game_res/cards/cut/card_medium_100'

SKIN_WATERMARK_URL = 'https://cbg-stzb.res.netease.com/game_res/cards/watermark/card_watermark_110'
HERO_WATERMARK_URL = 'https://cbg-stzb.res.netease.com/game_res/cards/watermark/card_watermark_100'


def dir_check():
    if not os.path.exists(SKIN_MEDIUM_PATH):
        os.makedirs(SKIN_MEDIUM_PATH)
    if not os.path.exists(HERO_MEDIUM_PATH):
        os.makedirs(HERO_MEDIUM_PATH)
    if not os.path.exists(SKIN_WATERMARK_PATH):
        os.makedirs(SKIN_WATERMARK_PATH)
    if not os.path.exists(HERO_WATERMARK_PATH):
        os.makedirs(HERO_WATERMARK_PATH)


def download_skin_pic():
    for i in range(1, SKIN_LATEST + 1):
        medium_resp = requests.get(f"{SKIN_MEDIUM_URL}{i:03d}.jpg")
        watermark_resp = requests.get(f"{SKIN_WATERMARK_URL}{i:03d}.jpg")
        if medium_resp.status_code == 200:
            with open(f'{SKIN_MEDIUM_PATH}card_medium_110{i:03d}.jpg', 'wb') as f1, \
                    open(f'{SKIN_WATERMARK_PATH}card_watermark_110{i:03d}.jpg', 'wb') as f2:
                f1.write(medium_resp.content)
                f2.write(watermark_resp.content)
                logger.info(f'Skin Pic Downloading: {i}/{SKIN_LATEST}')
    logger.info(f'Skin Pic Download Complete!')



def download_hero_pic():
    for i in range(1, HERO_LATEST + 1):
        medium_resp = requests.get(f"{HERO_MEDIUM_URL}{i:03d}.jpg")
        watermark_resp = requests.get(f"{HERO_WATERMARK_URL}{i:03d}.jpg")
        if medium_resp.status_code == 200:
            with open(f'{HERO_MEDIUM_PATH}card_medium_100{i:03d}.jpg', 'wb') as f1, \
                    open(f'{HERO_WATERMARK_PATH}card_watermark_100{i:03d}.jpg', 'wb') as f2:
                f1.write(medium_resp.content)
                f2.write(watermark_resp.content)
                logger.info(f'Hero Pic Downloading: {i}/{HERO_LATEST}')
    logger.info(f'Hero Pic Download Complete!')


if __name__ == '__main__':
    dir_check()
    download_hero_pic()
    download_skin_pic()