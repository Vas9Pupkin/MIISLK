from PyQt5 import QtCore, QtGui, QtWidgets
import sys
#import time

import dbconForD2In
from Par1 import Ui_MainWindow
from Par2 import Ui_MainWindow22
import dbconForD
from LassstOf import Ui_MainWindowLa
from Par4 import Ui_MainWindowPar4
from Par3 import Ui_MainWindowPar3
from Zapiwiiis import  Ui_MainWindowZapiw
from YdaliS import Ui_MainWindowYDA
from Ramka1 import Ui_MainWindowRamd1
from RamaLast import Ui_MainWindowRLA



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()












def openOtherWindow():
    global OMainWindow
    OMainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow22()
    ui.setupUi(OMainWindow)
    MainWindow.close()
    OMainWindow.show()

    def returnToMain():
        OMainWindow.close()
        MainWindow.show()



    def Registriryisa():
        c = (ui.lineEdit.text())
        d = (ui.lineEdit_2.text())
        v = (ui.lineEdit_3.text())
        f = (ui.comboBox.currentText())
        if d==v and f=="Пациент":
            try:
                dbconForD2In.qLo('id', 'Юзер', c)
                print('Логин занят так то')
                ui.label_7.setText('Логин уже занят')

            except:
                print('Daaa')
                dbconForD2In.q(c, d)
                print('ffuua')
                global MainWindowPar4
                MainWindowPar4 = QtWidgets.QMainWindow()
                uiPa4 = Ui_MainWindowPar4()
                uiPa4.setupUi(MainWindowPar4)
                OMainWindow.close()
                MainWindowPar4.show()

                def finalRegistr():
                    y = uiPa4.lineEdit_5.text()
                    yy = uiPa4.lineEdit_4.text()
                    yyy = uiPa4.lineEdit.text()
                    yyyy = uiPa4.lineEdit_2.text()
                    yyyyy = uiPa4.lineEdit_3.text()
                    try:
                        dbconForD2In.qZanDa(y,yy,yyy,yyyy,yyyyy)
                        Jo1=dbconForD.q("id", "Юзер", c, d)
                        Jo2=dbconForD.qJoJoJo(yyyy)
                        dbconForD2In.qJoJo123(Jo2,Jo1)
                        MainWindowPar4.close()
                        MainWindow.show()



                    except:
                        print('')


                uiPa4.pushButton_2.clicked.connect(finalRegistr)


        elif d==v and f=="Врач":
            print('fgh')
            try:
                dbconForD2In.qLo('id', 'Док', c)
                print('Логин занят так то')
                ui.label_7.setText('Логин уже занят')

            except:
                print('Daaa')
                print(c)
                print(d)
                #dbconForD2In.qVr(c, d)
                print('dfdfS')
                global MainWindowPar3
                MainWindowPar3 = QtWidgets.QMainWindow()
                uiPa3 = Ui_MainWindowPar3()
                uiPa3.setupUi(MainWindowPar3)
                OMainWindow.close()
                MainWindowPar3.show()

                def Na4alo():
                    MainWindowPar3.close()
                    MainWindow.show()

                def RegVraKo():
                    x=uiPa3.lineEdit_3.text()
                    xx=uiPa3.lineEdit_33.text()
                    if x=='ILOVEBH':
                        dbconForD2In.qVr(c,d,'Бх')
                        xxx=dbconForD.q('id','Док', c,d)
                        dbconForD2In.qVr222(xxx, xx, x)
                        MainWindowPar3.close()
                        MainWindow.show()
                    elif x=='ILOVEFD':
                        dbconForD2In.qVr(c,d,'Функц')
                        xxx = dbconForD.q('id', 'Док', c, d)
                        dbconForD2In.qVr222(xxx, xx, x)
                        MainWindowPar3.close()
                        MainWindow.show()
                    elif x=='ILOVEVA':
                        dbconForD2In.qVr(c,d,'Привив')
                        xxx = dbconForD.q('id', 'Док', c, d)
                        dbconForD2In.qVr222(xxx, xx, x)
                        MainWindowPar3.close()
                        MainWindow.show()
                    elif x=='ILOVEALL':
                        dbconForD2In.qVr(c,d,'Общ')
                        xxx = dbconForD.q('id', 'Док', c, d)
                        dbconForD2In.qVr222(xxx, xx, x)
                        MainWindowPar3.close()
                        MainWindow.show()
                    else:
                        MainWindowPar3.close()




                uiPa3.pushButton.clicked.connect(Na4alo)
                uiPa3.pushButton_2.clicked.connect(RegVraKo)
        else:
            ui.label_7.setText('Пароли не совпадают')











    ui.pushButton.clicked.connect(returnToMain)
    ui.pushButton_2.clicked.connect(Registriryisa)







def checkLoPa():
    c=(ui.lineEdit.text())
    d=(ui.lineEdit_2.text())







    try:
        n = dbconForD.q("id", "Док", c, d)
        print(n)
        global MainWindowRamd1
        MainWindowRamd1 = QtWidgets.QMainWindow()
        uiRamk1 = Ui_MainWindowRamd1()
        uiRamk1.setupUi(MainWindowRamd1)
        MainWindow.close()
        MainWindowRamd1.show()
        ggna15=dbconForD.qRam22(n)
        print('HHH')
        print(ggna15)
        try:
            portivse =dbconForD.qRam1(ggna15)
            uiRamk1.label_4.setText(portivse)
        except:
            portivse =''
            uiRamk1.label_4.setText('-')



        def naVihod():
            MainWindowRamd1.close()
            MainWindow.show()
        def RabSPa():
            print('SSMi')
            global MainWindowRLA
            MainWindowRLA = QtWidgets.QMainWindow()
            uiRLA = Ui_MainWindowRLA()
            uiRLA.setupUi(MainWindowRLA)
            MainWindowRamd1.close()
            MainWindowRLA.show()

            def OtkazOtPac():
                MainWindowRLA.close()
                MainWindowRamd1.show()

            def VSESk():

                Rezultat=(uiRLA.textEdit.toPlainText())
                dbconForD2In.qRLAPLZ(ggna15, portivse, Rezultat)
                vc=dbconForD.qRam2244(n)
                dbconForD2In.qVraPLZ(ggna15, portivse, vc)


                MainWindowRLA.close()




            uiRLA.pushButton.clicked.connect(OtkazOtPac)
            uiRLA.pushButton_2.clicked.connect(VSESk)





        uiRamk1.pushButton.clicked.connect(naVihod)
        uiRamk1.pushButton_2.clicked.connect(RabSPa)






    except:
        try:



            n = dbconForD.q("id", "Юзер", c, d)
            print(n)
            n=dbconForD.qJoJoLaSt(n)

            print('jncjcb')
            global MainWindowLa
            MainWindowLa = QtWidgets.QMainWindow()
            uiLast = Ui_MainWindowLa()
            print('ambas')
            uiLast.setupUi(MainWindowLa, n)
            print('adoor')
            MainWindow.close()
            MainWindowLa.show()




            def zAPISBNAPRIEM():
                print('ff')
                global MainWindowZapiw
                MainWindowZapiw = QtWidgets.QMainWindow()
                uiZapiw = Ui_MainWindowZapiw()
                uiZapiw.setupUi(MainWindowZapiw)
                MainWindowLa.close()
                MainWindowZapiw.show()


                def BtoLa():
                    MainWindowZapiw.close()
                    MainWindowLa.show()

                def RegBtoLa():
                    aqw=uiZapiw.comboBox.currentText()
                    aqw2=uiZapiw.lineEdit.text()
                    print('Этап1')

                    dbconForD2In.qZap(aqw,aqw2)
                    print('Этап2')
                    ParaPara=(dbconForD.qMAKS(aqw))
                    print('Этап3')
                    dbconForD2In.qZapolniTALON(aqw, str(ParaPara))
                    if dbconForD.qIDVNESI1(aqw, n)=='':
                        print('Этап4')
                        dbconForD2In.qVnesiEMKSETUP(aqw,str(ParaPara),n)
                        print('Этап5')
                    else:
                        print('SyperEtap')
                        ParaPara=(dbconForD.qIDVNESI1(aqw, n))+', '+str(ParaPara)
                        print(ParaPara)
                        print('SyperpyperEtap')
                        dbconForD2In.qVnesiEMKSETUP(aqw,ParaPara,n)

                    uiLast.setupUi(MainWindowLa, n)
                    uiLast.pushButton.clicked.connect(zAPISBNAPRIEM)
                    uiLast.pushButton_3.clicked.connect(YdaliPriem)
                    MainWindowZapiw.close()

                    MainWindowLa.show()






                uiZapiw.pushButton.clicked.connect(BtoLa)
                uiZapiw.pushButton_2.clicked.connect(RegBtoLa)

            def YdaliPriem():
                print('Этап1')
                global MainWindowYDA
                MainWindowYDA = QtWidgets.QMainWindow()
                uiYDA = Ui_MainWindowYDA()
                uiYDA.setupUi(MainWindowYDA)
                MainWindowLa.close()
                MainWindowYDA.show()

                def BtoLa():
                    MainWindowYDA.close()
                    MainWindowLa.show()


                def YdaLIL():
                    aqw = uiYDA.comboBox.currentText()
                    aqw2 = uiYDA.lineEdit.text()
                    print(aqw)
                    print(aqw2)

                    if dbconForD.qYDInfo(aqw,aqw2)=='':
                        dbconForD2In.qYDALYAEM(aqw, aqw2)

                        blalba=dbconForD.qIDVNESI1(aqw,n)
                        if len(blalba)>len(aqw2) and blalba.find(aqw2)+len(aqw2)==len(blalba):
                            blalba=blalba.replace(', '+aqw2,'',1)
                            print('E1')
                            print(blalba)
                            dbconForD2In.qVnesiEMKSETUP(aqw, blalba, n)
                        elif len(blalba)>len(aqw2):
                            blalba=blalba.replace(aqw2+', ','',1)
                            print('E2')
                            print(blalba)
                            dbconForD2In.qVnesiEMKSETUP(aqw, blalba, n)
                        else:
                            dbconForD2In.qVnesiEMKSETUP(aqw,'',n)
                            print('E3')
                            print(blalba)



                        uiYDA.pushButton_2.setText('Отменено')
                    else:
                        uiYDA.pushButton_2.setText('Просрочено')
                    uiLast.setupUi(MainWindowLa, n)
                    uiLast.pushButton.clicked.connect(zAPISBNAPRIEM)
                    uiLast.pushButton_3.clicked.connect(YdaliPriem)













                uiYDA.pushButton.clicked.connect(BtoLa)
                uiYDA.pushButton_2.clicked.connect(YdaLIL)







            uiLast.pushButton.clicked.connect(zAPISBNAPRIEM)
            uiLast.pushButton_3.clicked.connect(YdaliPriem)




        except:
            print("Error in Connection")
            ui.label_5.setText('Неверный логин или пароль')













ui.pushButton_2.clicked.connect(openOtherWindow)
ui.pushButton.clicked.connect(checkLoPa)










sys.exit(app.exec_())