import sys
import time
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 562)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 4, 0, 1, 2)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_2.addWidget(self.calendarWidget, 0, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 3, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_2.addWidget(self.timeEdit, 1, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Добавить напоминание"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить напоминание"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Минипланировщик+')
        self.list_1 = []
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delet)
        self.time_now = str(time.ctime()).split()[3]

    def initUi(self):
        pass  # без этого не работает
        # а если сюда засунуть кнопку, тоже ничего не сработает

    def add(self):
        if self.lineEdit.text():
            data = self.calendarWidget.selectedDate().toString('yyyy.MM.dd')
            time = self.timeEdit.time().toString('hh:mm')
            text_event = self.lineEdit.text()
            self.list_1.append((data, time, text_event))
            self.list_1.sort()
            self.listWidget.clear()
            for i in self.list_1:
                self.listWidget.addItem(str(i[0]) + ' (' + str(i[1]) + ') - ' + str(i[2]))

    def delet(self):
        if self.lineEdit.text():
            data = self.calendarWidget.selectedDate().toString('yyyy.MM.dd')
            time = self.timeEdit.time().toString('hh:mm')
            text_event = self.lineEdit.text()
            num = ''
            for n, i in enumerate(self.list_1, start=0):
                if (data, time, text_event) == i:
                    num = n
            if num != '':
                del self.list_1[num]
                self.list_1.sort()
                self.listWidget.clear()
                for i in self.list_1:
                    self.listWidget.addItem(str(i[0]) + ' (' + str(i[1]) + ') - ' + str(i[2]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
