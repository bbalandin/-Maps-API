import os
from PIL import Image

import requests
from PyQt5.QtGui import QPixmap
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt

SCREEN_SIZE = [600, 600]


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.start_window()
        self.pushButton.clicked.connect(self.Img)
        self.latitude_1 = 0
        self.longitude_1 = 0
        self.zoom_1 = 0

    def start_window(self):
        uic.loadUi('ui.ui', self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.latitude_1 += 1
            self.Img()
        if event.key() == Qt.Key_A:
            self.latitude_1 -= 1
            self.Img()
        if event.key() == Qt.Key_W:
            self.longitude_1 += 1
            self.Img()
        if event.key() == Qt.Key_S:
            self.longitude_1 -= 1
            self.Img()

    def Img(self):
        latitude = self.latitude.text()
        longitude = self.longitude.text()
        zoom = self.zoom.text()
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={float(latitude) + self.latitude_1},{float(longitude) + self.longitude_1}&spn={zoom},{zoom}&l=map"
        response = requests.get(map_request)
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.pixmap = QPixmap("map.png")
        self.map.setPixmap(self.pixmap)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())