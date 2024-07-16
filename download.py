import requests

SKIN_LATEST = 261
HERO_LATEST = 730

SKIN_MEDIUM_PATH = 'res/cards/medium/skin/'
HERO_MEDIUM_PATH = 'res/cards/medium/skin/'

SKIN_WATERMARK_PATH = 'res/cards/watermark/skin/'
HERO_WATERMARK_PATH = 'res/cards/watermark/hero/'

SKIN_MEDIUM_URL = 'https://cbg-stzb.res.netease.com/game_res/cards/cut/card_medium_110'
HERO_MEDIUM_URL = 'https://cbg-stzb.res.netease.com/game_res/cards/cut/card_medium_100'

SKIN_WATERMARK_URL = 'https://cbg-stzb.res.netease.com/game_res/cards/watermark/card_watermark_110'
HERO_WATERMARK_URL = 'https://cbg-stzb.res.netease.com/game_res/cards/watermark/card_watermark_100'


def download_medium_pic(skin_or_hero):
    # skin_or_hero = 1
    if (skin_or_hero):
        return





for i in range(1, 262):
    url = f"https://cbg-stzb.res.netease.com/game_res/cards/watermark/card_watermark_110{i:03d}.jpg"
    response = requests.get(url)
    if (response.status_code == 200):
            # 打开文件进行二进制写入
        with open(f'res/cards/watermark/skin/card_watermark_110{i:03d}.jpg', 'wb') as f:
            f.write(response.content)  # 写入图片内容
        print(f'{url} 保存成功')