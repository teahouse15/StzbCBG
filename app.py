from flask import Flask, request, render_template
import os
import webview

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_g_info', methods=['POST'])
def get_game_account_info():
    input_data = request.form.get('inputData')
    print(f"Received input: {input_data}")
    return input_data

if __name__ == '__main__':
    import threading
    threading.Thread(target=app.run, kwargs={'debug': False}).start()
    # webview.create_window("My Flask App", "http://localhost:5000", frameless=True, width=1100, height=800)
    # frameless窗口头 resizable不可修改
    webview.create_window("My Flask App", "http://localhost:5000", resizable=False, width=1200, height=800)
    # 打开开发者工具
    webview.start(debug=False)
