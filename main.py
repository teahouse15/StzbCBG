import webview

def main():
    # 创建一个简单的窗口，加载本地 HTML 文件
    window = webview.create_window("Simple Browser", "./web/main.html", fullscreen=True)
    webview.start()

if __name__ == '__main__':
    main()
