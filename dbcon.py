import pyodbc




def q(a,b,c):
    try:

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('SELECT ' +a+ ' FROM '+b +' WHERE id='+c)

        for row in cur.fetchall():
            m=1

        if str(row)=='(None,)':
            return ''
        else:
            return str(row)[1:len(str(row))-2]


    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''



def q2(a,b,c):
    try:

        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                     r'DBQ=C:\Users\MSI\Desktop\Python4\pp.accdb;'
        conn = pyodbc.connect(con_string)
        cur = conn.cursor()
        cur.execute('SELECT ' +a+ ' FROM '+b +' WHERE id='+c)


        for row in cur.fetchall():

            m=1
        if (str(row))!='(None,)':
            a = (str(row))
            a = a.replace('(', '')
            a = a.replace(')', '')
            a = a.replace(',', '')
            a = a.replace(' , ', '')
            a = a[1:len(a) - 1]
            a = a.split()
            return a
        else:
            return ''







    except pyodbc.Error as e:
        print("Error in Connection", e)
        return ''







if __name__ == "__main__":
   print(q("Название", "Прививочныйсертификат", '6'))



#newGreed.zxc()