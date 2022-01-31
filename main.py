import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.start_window()

    def start_window(self):
        uic.loadUi('ui.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

