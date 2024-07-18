from flask import Flask, render_template
import webview
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/close_window', methods=['POST'])
def close_window():
    # 在这里处理关闭窗口和结束进程的操作
    os.kill(os.getpid(), 9)  # 结束进程的示例方法，可根据实际情况调整
    return '', 204


if __name__ == '__main__':
    # Start Flask app in a separate thread
    import threading
    threading.Thread(target=app.run, kwargs={'debug': False}).start()

    # Open a webview window to display Flask app
    webview.create_window("My Flask App", "http://127.0.0.1:5000", frameless=True)
    webview.start()
