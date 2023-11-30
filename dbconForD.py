import pyodbc
def q(a,b,c, d):
    try:
        print('SELECT ' + a + ' FROM ' + b + ' WHERE Логин= ' + "'" + (c) + "'" + ' and Пароль=' + d)

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('SELECT ' +a+ ' FROM '+b +' WHERE Логин= '+ "'"+(c)+ "'" + ' and Пароль='+ "'"+d+ "'")


        for row in cur.fetchall():
            m=1
        return str(row)[1:len(str(row))-2]


    except pyodbc.Error as e:
        print("Error in ConnectionYaLox", e)
        return ''


def qRam1(a):
    if a=="Общ":
        a="Результатыпосещенийврача"

    elif a=="Функц":
        a="Функцдиагностика"

    elif a=="Бх":
        a="Лабдиагностика"

    else:
        a="Прививочныйсертификат"

    try:
        print("SELECT id FROM " + a +" WHERE Врач IS NULL")

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute("SELECT id FROM " + a +" WHERE Врач IS NULL")


        for row in cur.fetchall():
            m=1

        return str(row)[1:len(str(row))-2]


    except pyodbc.Error as e:
        print("Error in ConnectionYaLox", e)
        return ''

def qRam22(a):


    try:
        print("SELECT Тип FROM Док WHERE id="+a+"")

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute("SELECT Тип FROM Док WHERE id="+a+"")


        for row in cur.fetchall():
            m=1

        return str(row)[2:len(str(row))-3]


    except pyodbc.Error as e:
        print("Error in ConnectionYaLox", e)
        return ''


def qJoJoLaSt(a):


    try:
        print("SELECT IdEmk FROM IdEmPa WHERE IdUser="+a+"")

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute("SELECT IdEmk FROM IdEmPa WHERE IdUser="+a+"")


        for row in cur.fetchall():
            m=1

        return str(row)[1:len(str(row))-2]


    except pyodbc.Error as e:
        print("Error in ConnectionYaLox", e)
        return ''








def qRam2244(a):


    try:
        print("SELECT FIO FROM Всядокин WHERE id="+a+"")

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute("SELECT FIO FROM Всядокин WHERE id="+a+"")


        for row in cur.fetchall():
            m=1

        return str(row)[2:len(str(row))-3]


    except pyodbc.Error as e:
        print("Error in ConnectionYaLox", e)
        return ''



def qJoJoJo(a):


    try:
        print("SELECT id FROM Элмедкарта WHERE ИНН="+a+"")

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute("SELECT id FROM Элмедкарта WHERE ИНН="+a+"")


        for row in cur.fetchall():
            m=1

        return str(row)[1:len(str(row))-2]


    except pyodbc.Error as e:
        print("Error in ConnectionYaLox", e)
        return ''












def qMAKS(a):
    if a=="Общий":
        a="Результатыпосещенийврача"

    elif a=="Функц":
        a="Функцдиагностика"

    elif a=="Биохим":
        a="Лабдиагностика"

    else:
        a="Прививочныйсертификат"

    try:
        print('SELECT MAX(id) FROM ' + a )

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('SELECT MAX(id) FROM ' + a )


        for row in cur.fetchall():
            m=1
        return str(row)[1:len(str(row))-2]


    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''





def qIDVNESI1(a,b):
    if a=="Общий":
        a="Резпосещврача"

    elif a=="Функц":
        a="Функцисследование"

    elif a=="Биохим":
        a="Лабораторноеисследование"

    else:
        a="Вакцинация"

    try:
        print(('SELECT ' +a+ ' FROM Элмедкарта WHERE id='+b))

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('SELECT ' +a+ ' FROM Элмедкарта WHERE id='+b)

        for row in cur.fetchall():

            m=1


        if str(row)=='(None,)':
            return ''
        else:
            return str(row)[2:len(str(row))-3]


    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''







def qYDInfo(a,b):
    if a == "Общий":
        a = "Результатыпосещенийврача"

    elif a == "Функц":
        a = "Функцдиагностика"

    elif a == "Биохим":
        a = "Лабдиагностика"

    else:
        a = "Прививочныйсертификат"

    try:
        print(('SELECT Врач FROM '+a+' WHERE id='+b))

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('SELECT Врач FROM '+a+' WHERE id='+b)

        for row in cur.fetchall():

            m=1




        try:
            if str(row) == '(None,)':
                return ''
            else:
                return str(row)[1:len(str(row)) - 2]
        except:
            return ''



    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''








c="whoisyourdaddy"
d='yayaya'
print(c)
print(d)
if __name__ == "__main__":

   print(qJoJoLaSt('5'))


