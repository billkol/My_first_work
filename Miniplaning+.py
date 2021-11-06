import sys
import time
from random import randint
import threading
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 562)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 32, 0, 1, 3)
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_2.addWidget(self.timeEdit, 28, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 27, 0, 1, 2)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_2.addWidget(self.calendarWidget, 0, 0, 1, 3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 28, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 27, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 33, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 33, 2, 1, 1)
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
        self.pushButton_2.setText(_translate("MainWindow", "Delete reminder"))
        self.pushButton.setText(_translate("MainWindow", "Add reminder"))
        self.pushButton_3.setText(_translate("MainWindow", "Reminder search"))
        self.pushButton_4.setText(_translate("MainWindow", "Update"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        global list_1
        self.list_1 = list_1
        super(MyWidget, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Mini-planner+')
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delet)
        self.pushButton_3.clicked.connect(self.search)
        self.pushButton_4.clicked.connect(self.update)
        self.time_start = ':'.join(str(time.ctime()).split()[3].split(':')[:2])
        self.list_lokal = []
        self.count = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_2)
        self.timer.start(1000)

    def initUi(self):
        pass  # без этого не работает
        # а если сюда засунуть кнопку, тоже ничего не сработает

    def add(self):
        if self.lineEdit.text():
            data = self.calendarWidget.selectedDate().toString('dd.MM.yyyy')
            time = self.timeEdit.time().toString('hh:mm')
            text_event = self.lineEdit.text()
            self.list_1.append([data, time, text_event])
            self.list_1.sort()
            self.listWidget.clear()
            for i in self.list_1:
                self.listWidget.addItem(str(i[0]) + ' (' + str(i[1]) + ') - ' + str(i[2]))

    def delet(self):
        if self.lineEdit.text():
            data = self.calendarWidget.selectedDate().toString('dd.MM.yyyy')
            time = self.timeEdit.time().toString('hh:mm')
            text_event = self.lineEdit.text()
            num = ''
            for n, i in enumerate(self.list_1, start=0):
                if [data, time, text_event] == i:
                    num = n
            if num != '':
                del self.list_1[num]
                self.list_1.sort()
                self.listWidget.clear()
                for i in self.list_1:
                    self.listWidget.addItem(str(i[0]) + ' (' + str(i[1]) + ') - ' + str(i[2]))

    def search(self):
        list_search = []
        text_event = self.lineEdit.text()
        for i in self.list_1:
            if i[2] == text_event:
                list_search.append(str(i[0]) + ' (' + str(i[1]) + ') - ' + str(i[2]))
        self.listWidget.clear()
        for i in list_search:
            self.listWidget.addItem(i)

    def update(self):
        self.list_1.sort()
        self.listWidget.clear()
        for i in self.list_1:
            self.listWidget.addItem(str(i[0]) + ' (' + str(i[1]) + ') - ' + str(i[2]))
        self.list_lokal.clear()

    def timer_2(self):
        Current_Time = QTime.currentTime()
        self.time_now = Current_Time.toString('hh:mm')
        self.reminder()

    def reminder(self):
        for i in self.list_1:
            if self.count == 0 and i[1] == self.time_now:
                self.list_lokal.append(True)
        if len(self.list_lokal) > 0:
            if True in self.list_lokal:
                if self.count == 0:
                    self.open()
                    self.count += 1
        else:
            self.list_lokal.clear()
            self.count = 0
            self.open()

    def open(self):
        self.rem = Window_reminder()
        if True in self.list_lokal:
            self.rem.show()
        else:
            self.rem.close()


class Window_reminder(QWidget):
    def __init__(self):
        global list_1, ex
        self.list_1 = list_1
        self.ex = ex
        super(Window_reminder, self).__init__()
        self.setWindowTitle('Yeah, the time has come')
        self.setGeometry(500, 400, 500, 120)
        self.list_2 = ['Common, common, chop, chop',
                       'Are you ready?',
                       'Hey, stop sleeping',
                       'Hey, wake up dead!',
                       "They didn't give me a heart, so go do it, a bag of scythes",
                       "So, I've been thinking about it, and I decided that you need to do something"
                       " that you have planned for this time",
                       'I take it you need to do this on a list right now, right?',
                       "I'm a machine, and you're a person, maybe you managed to forget. "
                       "Here's a reminder",
                       "Maybe I'm wrong, but you wanted it yourself. Here you go",
                       "You haven't forgotten, have you? And if you forgot, here's a surprise box",
                       "Hey, he ran away here. Here, hold the reminder",
                       'So, either that or yes',
                       "My friend, here's my present for you",
                       "You wrote it down - do it",
                       "What's wrong? Getting active"]
        self.button = QPushButton(self)
        self.button.move(40, 70)
        self.button.resize(100, 30)
        self.button.setText('To do')
        self.button.clicked.connect(self.to_do)
        self.button2 = QPushButton(self)
        self.button2.move(350, 70)
        self.button2.resize(150, 30)
        self.button2.setText('set aside for 5 minutes')
        self.button2.clicked.connect(self.put_aside)
        self.text = QLabel(self)
        self.text.move(40, 20)
        num = randint(0, 14)
        self.text.setText(self.list_2[num])
        self.time_now = ':'.join(str(time.ctime()).split()[3].split(':')[:2])

    def to_do(self):
        num = -1
        for n, i in enumerate(self.list_1, start=0):
            if i[1] == self.time_now:
                num = n
        if num != -1:
            del self.list_1[num]
            self.ex.update()

    def put_aside(self):
        num = -1
        for n, i in enumerate(self.list_1, start=0):
            if i[1] == self.time_now:
                num = n
        if num != -1:
            if int(self.list_1[num][1].split(':')[1]) >= 55:
                if int(self.list_1[num][1].split(':')[0]) == 23:
                    if int(self.list_1[num][0].split('.')[1]) in [1, 3, 5, 7, 8, 10]:
                        if int(self.list_1[num][0].split('.')[2]) == 31:
                            self.list_1[num][0] = self.list_1[num][0].split('.')[0] + '.' + \
                                                  str(int(self.list_1[num][0].split('.')[1]) + 1)\
                                                  + '.01'
                            self.list_1[num][1] = '00:' + str(
                                int(self.list_1[num][0].split(':')[1]) - 55)
                        else:
                            self.list_1[num][0] = self.list_1[num][0].split('.')[0] + '.' + \
                                                  self.list_1[num][0].split('.')[1] + '.' + \
                                                  str(int(self.list_1[num][0].split('.')[1]) + 1)
                            self.list_1[num][1] = '00:' + str(
                                int(self.list_1[num][0].split(':')[1]) - 55)
                    elif int(self.list_1[num][0].split('.')[1]) in [4, 6, 9, 11]:
                        if int(self.list_1[num][0].split('.')[2]) == 30:
                            self.list_1[num][0] = self.list_1[num][0].split('.')[0] + '.' + \
                                                  str(int(self.list_1[num][0].split('.')[1]) + 1) \
                                                  + '.01'
                            self.list_1[num][1] = '00:' + str(
                                int(self.list_1[num][0].split(':')[1]) - 55)
                        else:
                            self.list_1[num][0] = self.list_1[num][0].split('.')[0] + '.' + \
                                                  self.list_1[num][0].split('.')[1] + '.' + \
                                                  str(int(self.list_1[num][0].split('.')[1]) + 1)
                            self.list_1[num][1] = '00:' + str(
                                int(self.list_1[num][0].split(':')[1]) - 55)
                    elif int(self.list_1[num][0].split('.')[1]) == 2:
                        if (int(self.list_1[num][0].split('.')[0]) / 4 ==
                                int(self.list_1[num][0].split('.')[0]) // 4 and
                                int(self.list_1[num][0].split('.')[0]) / 100 !=
                                int(self.list_1[num][0].split('.')[0]) // 100) or \
                                (int(self.list_1[num][0].split('.')[0]) / 400 ==
                                 int(self.list_1[num][0].split('.')[0]) // 400):
                            if int(self.list_1[num][0].split('.')[2]) == 29:
                                self.list_1[num][0] = self.list_1[num][0].split('.')[0] + '.' + \
                                                      str(int(self.list_1[num][0].split('.')[1])
                                                          + 1) + '.01'
                                self.list_1[num][1] = '00:' + str(
                                    int(self.list_1[num][0].split(':')[1]) - 55)
                            else:
                                self.list_1[num][0] = self.list_1[num][0].split('.')[0] + '.' + \
                                                      self.list_1[num][0].split('.')[1] + '.' + \
                                                      str(int(self.list_1[num][0].split('.')[1]) + 1)
                                self.list_1[num][1] = '00:' + str(
                                    int(self.list_1[num][0].split(':')[1]) - 55)
                        else:
                            if int(self.list_1[num][0].split('.')[2]) == 28:
                                self.list_1[num][0] = self.list_1[num][0].split('.')[0] + '.' + \
                                                      str(int(self.list_1[num][0].split('.')[1])
                                                          + 1) + '.01'
                                self.list_1[num][1] = '00:' + str(
                                    int(self.list_1[num][0].split(':')[1]) - 55)
                            else:
                                self.list_1[num][0] = self.list_1[num][0].split('.')[0] + '.' + \
                                                      self.list_1[num][0].split('.')[1] + '.' + \
                                                      str(int(self.list_1[num][0].split('.')[1]) + 1)
                                self.list_1[num][1] = '00:' + str(
                                    int(self.list_1[num][0].split(':')[1]) - 55)
                    elif int(self.list_1[num][0].split('.')[1]) == 12:
                        if int(self.list_1[num][0].split('.')[2]) == 31:
                            self.list_1[num][0] = str(int(self.list_1[num][0].split('.')[0]) + 1)\
                                                  + '01.01'
                            self.list_1[num][1] = '00:' + str(
                                int(self.list_1[num][0].split(':')[1]) - 55)
                else:
                    self.list_1[num][1] = str(int(self.list_1[num][1].split(':')[0]) + 1) \
                                          + ':' + str(int(self.list_1[num][0].split(':')[1]) - 55)
            else:
                self.list_1[num][1] = self.list_1[num][1].split(':')[0] + ':' + str(
                    int(self.list_1[num][1].split(':')[1]) + 5)
            self.ex.update()


if __name__ == '__main__':
    list_1 = []
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
