import sys,os
from PySide6.QtCore import Qt, QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QWebEngineView Disable Context Menu Example")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Create a QWebEngineView to display HTML content
        webview = QWebEngineView()
        layout.addWidget(webview)

        # Load local HTML file
        current_dir = os.path.dirname(__file__)
        html_filename = "templates/main.html"
        html_path = os.path.join(current_dir, html_filename)
        webview.load(QUrl.fromLocalFile(html_path))

        # Disable right-click context menu
        webview.setContextMenuPolicy(Qt.NoContextMenu)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
