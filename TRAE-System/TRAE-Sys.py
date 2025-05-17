import sys
import time

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget, QVBoxLayout, \
    QGroupBox, QRadioButton, QHBoxLayout, QGridLayout, QStackedLayout, QScrollArea, QFileDialog

from threading import Thread

# 正确导入 FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("./TRAE-System02.ui")
        self.ui.setWindowTitle("可溯源可逆对抗样本系统")
        self.ui.setWindowIcon(QIcon("HNU-icon.jpg"))

        self.ui.btn_tab1_openImg.clicked.connect(self.show_image)

        # 显示柱状图
        self.matplotlib_widget = MatplotlibWidget()
        layout = QVBoxLayout(self.ui.widget_tab3_resultOfTest)
        layout.addWidget(self.matplotlib_widget)

    def show_image(self):
        # 打开图片文件
        imgName, imgType = QFileDialog.getOpenFileName(self, "选择图片", "", "Image Files (*.jpg *.png)")
        img = QtGui.QPixmap(imgName).scaled(self.ui.label_tab1_oriImg.width(), self.ui.label_tab1_oriImg.height())
        self.ui.label_tab1_oriImg.setPixmap(img)
        self.ui.label_tab1_oriImg.setScaledContents(True)   # 自适应QLabel大小

        self.ui.label_tab1_TRAEImg.setPixmap(img)
        self.ui.label_tab1_TRAEImg.setScaledContents(True)  # 自适应QLabel大小

        self.ui.label_tab2_TRAEImg.setPixmap(img)
        self.ui.label_tab2_TRAEImg.setScaledContents(True)  # 自适应QLabel大小
        self.ui.label_tab2_recoveredImg.setPixmap(img)
        self.ui.label_tab2_recoveredImg.setScaledContents(True)  # 自适应QLabel大小

        self.ui.label_tab3_imgToBeTested.setPixmap(img)
        self.ui.label_tab3_imgToBeTested.setScaledContents(True)  # 自适应QLabel大小
        self.ui.lineEdit_tab2_extractMsg.setPlaceholderText("hainan")


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = Figure(figsize=(3, 3))
        self.canvas = FigureCanvas(self.figure)
        self.init_plot()
        layout = QVBoxLayout()
        # 设置边距为0
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def init_plot(self):
        ax = self.figure.add_subplot(111)
        ax.bar(['pelican', 'bath towel', 'spoonbill', 'black swan', 'U.S. egret'], [0.87, 0.82, 0.73, 0.67, 0.65])  # 示例数据

        # 设置 x, y 轴刻度标签的大小
        ax.tick_params(axis='y', labelsize=7)  # 可以根据需要调整标签大小
        ax.tick_params(axis='x', labelsize=7, labelrotation=60)  # 可以根据需要调整标签大小

        # 调整子图边距，参数为left边界位于x轴的百分比
        self.figure.subplots_adjust(left=0.15, right=0.96, top=0.98, bottom=0.29)

        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    # 展示窗口
    w.ui.show()

    app.exec_()

