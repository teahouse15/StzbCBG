from flask import Flask, render_template
import os
import webview

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/close_window', methods=['POST'])
def close_window():
    os.kill(os.getpid(), 9)
    return '', 204

@app.route('/minimize_window', methods=['POST'])
def minimize_window():
    webview.windows[0].minimize()
    return '', 204

@app.route('/maximize_window', methods=['POST'])
def maximize_window():
    webview.windows[0].toggle_fullscreen()
    return '', 204


if __name__ == '__main__':
    import threading
    threading.Thread(target=app.run, kwargs={'debug': False}).start()
    # webview.create_window("My Flask App", "http://localhost:5000", frameless=True, width=1100, height=800)
    # frameless窗口头 resizable不可修改
    webview.create_window("My Flask App", "http://localhost:5000", frameless=False, resizable=True, width=1100, height=800)
    webview.start()
