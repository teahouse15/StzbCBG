from flask import Flask, request, render_template
import os
import webview
import funcs

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_account_info', methods=['POST'])
def get_game_account_info():
    url = request.form.get('url')
    account_total, account_information, hero_list = funcs.request_account_information(url)
    print(account_total)

    for hero in hero_list:
        """
            {
            	'hit_range': 2,
            	'hero_type_advance': 0,
            	'name': '卫瓘',
            	'cfg_hero_type_availible': [12, 22],
            	'awake_state': 0,
            	'country': 6,
            	'card_border': '',
            	'is_season_card': 0,
            	'advance_num': 0,
            	'hero_type_availible': [],
            	'hero_type': 2,
            	'dynamic_icon': 0,
            	'is_support': False,
            	'cost': 3.0,
            	'season': 'N',
            	'policy_awake_state': 0,
            	'icon_hero_id': 100707,
            	'hero_features': 0,
            	'quality': 5,
            	'army_facade': [],
            	'hero_id': 100707
            }
        """

    return url


if __name__ == '__main__':
    import threading

    threading.Thread(target=app.run, kwargs={'debug': False}).start()
    # webview.create_window("My Flask App", "http://localhost:5000", frameless=True, width=1100, height=800)
    # frameless窗口头 resizable不可修改
    webview.create_window("My Flask App", "http://localhost:5000", resizable=False, width=1200, height=800)
    # 打开开发者工具
    webview.start(debug=False)
