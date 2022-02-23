from PyQt5 import QtWidgets  # Импортирование из библиотеки PyQt5 классов
# Импортирование из библиотеки PyQt5.QtWidgets классов
from PyQt5.QtWidgets import QPushButton, QSpinBox, QTableWidget, QMessageBox

# Основной класс формы для ввода координат
class Ui_Point(object):

    # Создание списка для записи координат точек
    data = []

    def setupUi(self, Point):
        Point.setObjectName("Point")
        Point.setFixedSize(300, 300)
        self.centralwidget = QtWidgets.QWidget(Point)
        self.centralwidget.setObjectName("centralwidget")
        # Создаём spinbox для изменения числа строк таблицы
        self.spin = QSpinBox(self)
        self.spin.move(10, 10)
        self.spin.setMaximum(10)
        self.spin.setMinimum(3)
        self.spin.valueChanged.connect(self.change)

        # Создаём таблицу 2 столбца, число строк имзеняемое, начиная с 1
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setRowCount(int(self.spin.text()))
        self.table.setHorizontalHeaderLabels(["Введите x", "Введите y"])

        self.table.move(20, 60)

        # Делаем кнопку, по нажатию которой мы должны передаём данные дальше в обработку
        self.btn_1 = QPushButton("Добавить точки", self)
        self.btn_1.move(60, 10)
        self.btn_1.resize(110, 30)
        self.btn_1.clicked.connect(self.get_data)

        self.btn_2 = QPushButton("Очистить таблицу", self)
        self.btn_2.move(170, 10)
        self.btn_2.resize(120, 30)
        self.btn_2.clicked.connect(self.clear)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Ввод точек")
        self.show()

    def change(self):
        self.table.setRowCount(int(self.spin.text()))

    # Функция для получения списка коодинат точек из таблицы
    def get_data(self):

        rows = self.table.rowCount()
        cols = self.table.columnCount()

        try:
            for row in range(rows):
                tmp = []
                for col in range(cols):
                    tmp.append(int(self.table.item(row, col).text()))

                self.data.append(tmp)
            return self.data

        except:
            # Вывод сообщения о неверном вводе данных
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Необходимо ввести координаты точек численного типа')
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            error.setInformativeText('Для построение МВО нужны координаты точек')


            error.exec_()

    # Функция удаления данных из таблицы
    def clear(self):
        self.table.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Point = QtWidgets.QMainWindow()
    ui = Ui_Point()
    ui.setupUi(Point)
    Point.show()
    sys.exit(app.exec_())
    data
