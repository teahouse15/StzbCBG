from flask import Flask, request, render_template
import os
import webview
import funcs

app = Flask(__name__, static_folder='res')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/load-info')
def load_content():
    url = request.args.get('url')
    account_total, hero_info, skin_info, skill_info, gear_info = funcs.request_account_information(url)
    print(account_total)
    data = {
        'info': funcs.get_account_information(account_total),
        'hero_info': funcs.get_detail_hero_list(hero_info),
        'skin_info': skin_info,
        'skill_info': skill_info,
        'gear_info': gear_info
    }
    return render_template('main-content.html', data=data)

@app.template_filter('divide_by_100')
def divide_by_100(value):
    try:
        return f"{float(value) / 100:.2f}"
    except (ValueError, TypeError):
        return "0.00"


if __name__ == '__main__':
    import threading

    threading.Thread(target=app.run, kwargs={'debug': False}).start()
    # webview.create_window("My Flask App", "http://localhost:5000", frameless=True, width=1100, height=800)7
    # frameless窗口头 resizable不可修改
    webview.create_window("小小藏宝阁", "http://localhost:5000", resizable=False, width=1200, height=800)
    # 打开开发者工具
    webview.start(debug=True)
