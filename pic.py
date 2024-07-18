import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("区域展示图片示例")

        # 创建 QGraphicsView 和 QGraphicsScene
        self.view = QGraphicsView(self)
        self.scene = QGraphicsScene(self)

        # 加载图片并添加到场景
        pixmap = QPixmap("static/res/cards/medium/hero/card_medium_100003.jpg")  # 替换为图片路径
        scaled_pixmap = pixmap.scaled(133, 197)  # 设置为130x200大小
        pixmap_item = QGraphicsPixmapItem(scaled_pixmap)
        self.scene.addItem(pixmap_item)

        # 设置场景和视图
        self.view.setScene(self.scene)
        self.setCentralWidget(self.view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(1100, 800)
    window.show()
    sys.exit(app.exec())