# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3eee.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowPar3(object):
    def setupUi(self, MainWindowPar3):
        MainWindowPar3.setObjectName("MainWindowPar3")
        MainWindowPar3.resize(292, 609)
        MainWindowPar3.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindowPar3)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(95, 90, 110, 110))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:/Users/MSI/Desktop/Python4/medphotof.png"))
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 520, 271, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(45, 310, 202, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_33.setGeometry(QtCore.QRect(45, 360, 202, 20))
        self.lineEdit_33.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(95, 240, 102, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindowPar3.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindowPar3)
        self.statusbar.setObjectName("statusbar")
        MainWindowPar3.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowPar3)
        QtCore.QMetaObject.connectSlotsByName(MainWindowPar3)


    def retranslateUi(self, MainWindowPar3):
        _translate = QtCore.QCoreApplication.translate
        MainWindowPar3.setWindowTitle(_translate("MainWindowPar3", "MainWindowPar3"))
        self.pushButton.setText(_translate("MainWindowPar3", "Назад"))
        self.pushButton_2.setText(_translate("MainWindowPar3", "Зарегистрировать"))
        self.label_5.setText(_translate("MainWindowPar3", "<html><head><title>line-height</title></head><body><p>Введите код</p></body></html>"))







