import pyodbc
def q(a,b):
    try:
        print('INSERT INTO Юзер (Логин, Пароль) VALUES ('+"'"+a+"'"+', '+"'"+b+"'"+"'"+"'"+"'"+"'"+')')

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('INSERT INTO Юзер (Логин, Пароль) VALUES ('+"'"+a+"'"+', '+"'"+b+"'"+')')
        conn.commit()



        return


    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''


def qVr(a,b, c):
    try:
        print('INSERT INTO Док (Логин, Пароль,Тип) VALUES ('+"'"+a+"'"+', '+"'"+b+"'"+', '+"'"+c+"'"+')')

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('INSERT INTO Док (Логин, Пароль,Тип) VALUES ('+"'"+a+"'"+', '+"'"+b+"'"+', '+"'"+c+"'"+')')
        conn.commit()



        return


    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''






def qJoJo123(a,b):
    try:
        print('INSERT INTO IdEmPa VALUES ('+"'"+a+"'"+', '+"'"+b+"'"+')')

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('INSERT INTO IdEmPa VALUES ('+"'"+a+"'"+', '+"'"+b+"'"+')')
        conn.commit()



        return


    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''













def qZap(a,b):
    if a=="Общий":
        a="Результатыпосещенийврача"
        f="Дата"
    elif a=="Функц":
        a="Функцдиагностика"
        f="Датаисследования"
    elif a=="Биохим":
        a="Лабдиагностика"
        f="Датаисследования"
    else:
        a="Прививочныйсертификат"
        f="Датапрививания"





    try:
        print('INSERT INTO ' +a+' ('+ f+' ) VALUES ('+"'"+b+"'"+')')

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('INSERT INTO ' +a+' ('+ f+' ) VALUES ('+"'"+b+"'"+')')
        conn.commit()
        return
    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''



def qZapolniTALON(a,b):
    if a=="Общий" or a=="Общ":
        a="Результатыпосещенийврача"
        f="Заключение"
    elif a=="Функц":
        a="Функцдиагностика"
        f="Результат"
    elif a=="Биохим" or a=="Бх":
        a="Лабдиагностика"
        f="Результат"
    else:
        a="Прививочныйсертификат"
        f="Датаокончания"





    try:
        print('UPDATE '+a+' SET '+f+'='+b+' WHERE id='+b)

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('UPDATE '+a+' SET '+f+'='+b+' WHERE id='+b)
        conn.commit()
        return
    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''
















def qRLAPLZ(a,b, c):
    if a=="Общий" or a=="Общ":
        a="Результатыпосещенийврача"
        f="Заключение"
    elif a=="Функц":
        a="Функцдиагностика"
        f="Результат"
    elif a=="Биохим" or a=="Бх":
        a="Лабдиагностика"
        f="Результат"
    else:
        a="Прививочныйсертификат"
        f="Датаокончания"





    try:
        print("UPDATE "+a+" SET "+f+"="+"'"+c+"'"+" WHERE id="+b)

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute("UPDATE "+a+" SET "+f+"="+"'"+c+"'"+" WHERE id="+b)
        conn.commit()
        return
    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''




def qVraPLZ(a,b, c):
    f = "Врач"
    if a=="Общий" or a=="Общ":
        a="Результатыпосещенийврача"

    elif a=="Функц":
        a="Функцдиагностика"

    elif a=="Биохим" or a=="Бх":
        a="Лабдиагностика"

    else:
        a="Прививочныйсертификат"






    try:
        print("UPDATE "+a+" SET "+f+"="+"'"+c+"'"+" WHERE id="+b)

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute("UPDATE "+a+" SET "+f+"="+"'"+c+"'"+" WHERE id="+b)
        conn.commit()
        return
    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''

















def qVr222(a,b, c):
    try:
        print('INSERT INTO Всядокин VALUES ('+"'"+a+"'"+', '+"'"+b+"'"+', '+"'"+c+"'"+')')

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('INSERT INTO Всядокин VALUES ('+"'"+a+"'"+', '+"'"+b+"'"+', '+"'"+c+"'"+')')
        conn.commit()



        return

    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''




def qVnesiEMK(a,b):
    if a == "Общий":
        a = "Резпосещврача"

    elif a == "Функц":
        a = "Функцисследование"

    elif a == "Биохим":
        a = "Лабораторноеисследование"

    else:
        a = "Вакцинация"





    try:
        print('INSERT INTO Элмедкарта ('+ a+' ) VALUES ('+"'"+b+"'"+')')

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('INSERT INTO Элмедкарта ('+ a+' ) VALUES ('+"'"+b+"'"+')')
        conn.commit()
        return
    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''


def qVnesiEMKSETUP(a,b,c):
    if a == "Общий":
        a = "Резпосещврача"

    elif a == "Функц":
        a = "Функцисследование"

    elif a == "Биохим":
        a = "Лабораторноеисследование"

    else:
        a = "Вакцинация"

    try:
        print("UPDATE Элмедкарта SET "+a+"="+"'"+b+"'"+" WHERE id="+c)

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        print('Etap1')
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        print('Etap2')
        cur.execute("UPDATE Элмедкарта SET "+a+"="+"'"+b+"'"+" WHERE id="+c)
        print('Etap3')
        conn.commit()
        print('Etap4')
        return
    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''






def qLo(a,b,c):
    try:


        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('SELECT ' +a+ ' FROM '+b +' WHERE Логин= '+ "'"+(c)+ "'" )


        for row in cur.fetchall():
            m=1
        return str(row)[1:len(str(row))-2]


    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''







def qYDALYAEM(a,b):
    if a == "Общий":
        a = "Результатыпосещенийврача"

    elif a == "Функц":
        a = "Функцдиагностика"

    elif a == "Биохим":
        a = "Лабдиагностика"

    else:
        a = "Прививочныйсертификат"





    try:
        print('DELETE FROM '+a+' WHERE ID='+b)

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('DELETE FROM '+a+' WHERE ID='+b)
        conn.commit()
        return
    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''





def qZanDa(z,x,c,v,b):
    try:
        print('INSERT INTO Элмедкарта (ФИО, Паспортныеданные, Номерполиса, ИНН, Датарождения) VALUES ('+"'"+z+"'"+', '+"'"+x+"'"+', '+"'"+c+"'"+', '+"'"+v+"'"+', '+"'"+b+"'"+')')

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('INSERT INTO Элмедкарта (ФИО, Паспортныеданные, Номерполиса, ИНН, Датарождения) VALUES ('+"'"+z+"'"+', '+"'"+x+"'"+', '+"'"+c+"'"+', '+"'"+v+"'"+', '+"'"+b+"'"+')')
        conn.commit()



        return


    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''






z='Фрыганов И.И.'
x='34356464655'
c='4534523'
v='22343433'
b='17/12/1999'
t='Fdagonfftime'
tt='qwety'
ttt='Общ'
j='3'
jj='Валет В.В.'
jjj=t
if __name__ == "__main__":
    qJoJo123('2','3')

