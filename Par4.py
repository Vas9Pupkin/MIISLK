# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '45eee.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowPar4(object):
    def setupUi(self, MainWindowPar4):
        MainWindowPar4.setObjectName("MainWindowPar4")
        MainWindowPar4.resize(291, 609)
        MainWindowPar4.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindowPar4)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(95, 90, 110, 110))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("medphotof.png"))
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 520, 271, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 382, 202, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 375, 59, 27))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 341, 202, 20))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(10, 335, 71, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 435, 202, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 410, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 305, 202, 20))
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 275, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 260, 59, 27))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 264, 202, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        MainWindowPar4.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindowPar4)
        self.statusbar.setObjectName("statusbar")
        MainWindowPar4.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowPar4)
        QtCore.QMetaObject.connectSlotsByName(MainWindowPar4)

    def retranslateUi(self, MainWindowPar4):
        _translate = QtCore.QCoreApplication.translate
        MainWindowPar4.setWindowTitle(_translate("MainWindowPar4", "MainWindowPar4"))

        self.pushButton_2.setText(_translate("MainWindowPar4", "Зарегистрировать"))
        self.label_3.setText(_translate("MainWindowPar4", "ИНН"))
        self.label_2.setText(_translate("MainWindowPar4", "Полис"))
        self.label_5.setText(_translate("MainWindowPar4", "<html><head>\n"
"  <meta charset=\"utf-8\">\n"
"  <title>line-height</title>\n"
"  <style>\n"
"   p {\n"
"    line-height: 0.4;\n"
"   }\n"
"  </style>\n"
" </head> <body><p>Дата</p><p>рож.</p></body></html>"))
        self.label_8.setText(_translate("MainWindowPar4", "<html><head>\n"
"  <meta charset=\"utf-8\">\n"
"  <title>line-height</title>\n"
"  <style>\n"
"   p {\n"
"    line-height: 0.4;\n"
"   }\n"
"  </style>\n"
" </head> <body><p>Паспор.</p><p>дан.</p></body></html>"))
        self.label_6.setText(_translate("MainWindowPar4", "ФИО"))



