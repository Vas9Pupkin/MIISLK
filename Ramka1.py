# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Rama2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowRamd1(object):
    def setupUi(self, MainWindowRamd1):
        MainWindowRamd1.setObjectName("MainWindowRamd1")
        MainWindowRamd1.resize(734, 825)
        MainWindowRamd1.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindowRamd1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 50, 381, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(40, 290, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(27)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(310, 290, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(27)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 740, 110, 29))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 740, 153, 29))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindowRamd1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowRamd1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 21))
        self.menubar.setObjectName("menubar")
        MainWindowRamd1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowRamd1)
        self.statusbar.setObjectName("statusbar")
        MainWindowRamd1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowRamd1)
        QtCore.QMetaObject.connectSlotsByName(MainWindowRamd1)

    def retranslateUi(self, MainWindowRamd1):
        _translate = QtCore.QCoreApplication.translate
        MainWindowRamd1.setWindowTitle(_translate("MainWindowRamd1", "MainWindowRamd1"))
        self.label.setText(_translate("MainWindowRamd1", "Следующий пациент"))
        self.label_3.setText(_translate("MainWindowRamd1", "№ Талона"))
        self.label_4.setText(_translate("MainWindowRamd1", "1"))
        self.pushButton.setText(_translate("MainWindowRamd1", "Выйти"))
        self.pushButton_2.setText(_translate("MainWindowRamd1", "Принять"))


