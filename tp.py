from PyQt5.uic import *
from PyQt5.QtWidgets import *
import sys



class MainWindow(QMainWindow):
    def init(self, parent=None):
        super().init(parent)
        loadUi('mainwin.ui',self)
        self.setCentralWidget(QPushButton('BEGIN'))



if __name__ == 'main':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
