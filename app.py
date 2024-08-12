from flask import Flask, render_template
import os
import webview

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/close_window', methods=['POST'])
def close_window():
    # 关闭 webview 窗口
    webview.windows[0].destroy()
    os._exit(0)
    return '', 204

if __name__ == '__main__':
    import threading
    threading.Thread(target=app.run, kwargs={'debug': False}).start()
    # webview.create_window("My Flask App", "http://localhost:5000", frameless=True, width=1100, height=800)
    # frameless窗口头 resizable不可修改
    webview.create_window("My Flask App", "http://localhost:5000", frameless=True, resizable=True, width=1100, height=800)
    # 打开开发者工具
    webview.start(debug=True)
