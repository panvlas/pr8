import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView

ans = ['', '', '']

# form1
class welcome(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(welcome, self).__init__()
        uic.loadUi('forms/welcome.ui', self)

        self.setWindowTitle('Окно приветсвия')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.Exit.clicked.connect(self.close)
        self.welcomeStart.clicked.connect(self.next)

    def next(self):
        self.switch_window.emit('1>2')

# form2 comboBox
class chilhood(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(chilhood, self).__init__()
        uic.loadUi('forms/chilhood.ui', self)

        self.setWindowTitle('Окно Детство')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.label_img.setPixmap(QPixmap('images/kasha.jpg'))
        self.label_img.setScaledContents(True)

        if ans[0] is not None:
            self.chilhoodLbl1.setText('Выбрано: ' + ans[0])

        self.comboBox.activated.connect(self.handleActivated)
        self.Back.clicked.connect(self.back)
        self.Next.clicked.connect(self.next)

    def handleActivated(self, index):
        ans[0] = self.comboBox.itemText(index)
        self.chilhoodLbl1.setText('Выбрано: ' + ans[0])

    def back(self):
        self.switch_window.emit('1<2')

    def next(self):
        self.switch_window.emit('2>3')

# form3 QTableWidget
class boyhood(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(boyhood, self).__init__()
        uic.loadUi('forms/boyhood.ui', self)

        self.setWindowTitle('Окно Отрочество')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.labelImg.setPixmap(QPixmap('images/karandash.jpg'))
        self.labelImg.setScaledContents(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        maxRows = self.tableWidget.rowCount()
        maxColumns = self.tableWidget.columnCount()
        tableWidth = self.tableWidget.geometry().width()
        tableHeight = self.tableWidget.geometry().height()
        row = 0
        col = 0
        while row < maxRows:
            self.tableWidget.setRowHeight(row, tableHeight / maxRows)
            row += 1
        while col < maxColumns:
            self.tableWidget.setColumnWidth(col, tableWidth / maxColumns)
            col += 1
        # if data[2][1] >= 0:
        #     self.boyhoodLbl1.setText(data[2][0])
        #     self.tableWidget.setCurrentCell(data[2][1], 0)
        self.tableWidget.itemSelectionChanged.connect(self.itemSelect)
        self.Back.clicked.connect(self.back)
        self.Next.clicked.connect(self.next)

    def itemSelect(self):
        print('here')
        ans[1] = self.tableWidget.currentItem().text()
        self.boyhoodLbl1.setText('Выбрано: '+self.tableWidget.currentItem().text())

    def back(self):
        self.switch_window.emit('2<3')

    def next(self):
        self.switch_window.emit('3>4')

# form4 QListWidget
class youth(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(youth, self).__init__()
        uic.loadUi('forms/youth.ui', self)

        self.setWindowTitle('Окно Юность')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.label_img.setPixmap(QPixmap('images/obraz.png'))
        self.label_img.setScaledContents(True)

        if ans[2] is not None:
            self.YouthLbl1.setText('Выбрано: ' + ans[2])

        self.blalistWidget.itemClicked.connect(self.item_click)
        self.Back.clicked.connect(self.back)
        self.Next.clicked.connect(self.next)

    def item_click(self, item):
        ans[2] = item.text()
        self.YouthLbl1.setText('Выбрано: ' + ans[2])

    def back(self):
        self.switch_window.emit('3<4')

    def next(self):
        self.switch_window.emit('4>5')

# form5 QTableWidget
class finish(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(finish, self).__init__()
        uic.loadUi('forms/finish.ui', self)

        self.setWindowTitle('Окно Спасибо')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        maxRows = self.tableWidget.rowCount()
        maxColumns = self.tableWidget.columnCount()
        tableWidth = self.tableWidget.geometry().width()
        tableHeight = self.tableWidget.geometry().height()
        row = 0
        col = 0
        while row < maxRows:
            self.tableWidget.setRowHeight(row, tableHeight / maxRows - 21)
            row += 1
        while col < maxColumns:
            self.tableWidget.setColumnWidth(col, tableWidth / maxColumns)
            col += 1
        self.tableWidget.setItem(0, 1, QTableWidgetItem(ans[0]))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(ans[1]))
        self.tableWidget.setItem(2, 1, QTableWidgetItem(ans[2]))
        self.Back.clicked.connect(self.back)
        self.Exit.clicked.connect(self.close)

    def back(self):
        self.switch_window.emit("4<5")

class Controller:
    def __init__(self):
        pass

    def select_forms(self, text):
        if text == '1':
            self.form1 = welcome()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()

        if text == '1>2':
            self.form2 = chilhood()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
            self.form1.close()

        if text == '2>3':
            self.form3 = boyhood()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
            self.form2.close()

        if text == '3>4':
            self.form4 = youth()
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
            self.form3.close()

        if text == '4>5':
            self.form5 = finish()
            self.form5.switch_window.connect(self.select_forms)
            self.form5.show()
            self.form4.close()

        if text == '4<5':
            self.form4 = youth()
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
            self.form5.close()

        if text == '3<4':
            self.form3 = boyhood()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
            self.form4.close()

        if text == '2<3':
            self.form2 = chilhood()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
            self.form3.close()

        if text == '1<2':
            self.form1 = welcome()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()
            self.form2.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.select_forms("1")
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
