import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PySide6.QtCore import Qt
import requests
import funcs



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("藏宝阁账号查询")
        self.resize(400, 300)
        self.center()

        # 创建主布局
        main_layout = QVBoxLayout()

        # 创建水平布局
        h_layout = QHBoxLayout()

        # 创建输入框和按钮
        self.url_text = QLineEdit(self)
        self.url_text.setPlaceholderText("请输入内容")
        self.confirm_button = QPushButton("查询", self)
        self.confirm_button.clicked.connect(self.display_text)

        # 将输入框和按钮添加到水平布局
        h_layout.addWidget(self.url_text)
        h_layout.addWidget(self.confirm_button)

        # 创建输出信息的文本框
        self.output_field = QTextEdit(self)
        self.output_field.setReadOnly(True)

        # 将水平布局和输出信息文本框添加到主布局
        main_layout.addLayout(h_layout)
        main_layout.addWidget(self.output_field)

        # 设置主布局
        self.setLayout(main_layout)

    # 查看账号
    def display_text(self):
        url = self.url_text.text()
        ordersn = funcs.get_account_ordersn(url)



        self.output_field.setText(ordersn)



    def center(self):
        screen = QApplication.primaryScreen().availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen.center())
        self.move(window_geometry.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
