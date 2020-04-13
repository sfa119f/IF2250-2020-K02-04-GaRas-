import mysql.connector

Pass = ""
Db = ""

def SetDB(user, data):
    global Pass
    global Db
    Pass = user
    Db = data
    UseDB()

def CreateDB(user, data):
    try:
        global Pass
        global Db
        Pass = user
        Db = data
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=Pass
        )
        mycursor = mydb.cursor()
        sql = "Create Database " + Db
        mycursor.execute(sql)
        UseDB()
    except mysql.connector.Error as e:
        print("Gagal menambah basis data : {}".format(e))

def UseDB():
    try:
        global Pass
        global Db
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=Pass,
            database=Db
        )
        mycursor = mydb.cursor()
        f = open("../Garas.sql")
        sql = f.read()
        mycursor.execute(sql, multi=True)
        
    except mysql.connector.Error as e:
        print("Gagal menggunakan basis data : {}".format(e))
        

def UpdateStok(a, b):
    try:
        global Pass
        global Db
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=Pass,
            database=Db
        )
        mycursor = mydb.cursor()

        sql1 = "Update produk set stok = %s where nama = %s"
        val1 = (b, a)

        mycursor.execute(sql1, val1)
        mydb.commit()
        print("Berhasil mengubah stok produk!")
    except mysql.connector.Error as e:
        print("Gagal mengubah stok produk : {}".format(e))

def UpdateSpek(a, b):
    try:
        global Pass
        global Db
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=Pass,
            database=Db
        )
        myc = mydb.cursor()
        sql1 = "Update produk set spek = %s where nama = %s"
        val1 = (b, a)

        myc.execute(sql1, val1)
        mydb.commit()
        print("Berhasil mengubah spek produk!")
    except mysql.connector.Error as e:
        print("Gagal mengubah spek produk : {}".format(e))

def UpdateHarga(a, b):
    try:
        global Pass
        global Db
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=Pass,
            database=Db
        )
        myc = mydb.cursor()
        sql1 = "Update produk set harga = %s where nama = %s"
        val1 = (b, a)

        myc.execute(sql1, val1)
        mydb.commit()
        print("Berhasil mengubah harga produk!")
    except mysql.connector.Error as e:
        print("Gagal mengubah harga produk : {}".format(e))

def UpdateNama(a, b):
    try:
        global Pass
        global Db
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=Pass,
            database=Db
        )
        myc = mydb.cursor()
        sql1 = "Update produk set nama = %s where nama = %s"
        val1 = (b, a)

        myc.execute(sql1, val1)
        mydb.commit()
        print("Berhasil mengubah nama produk!")
    except mysql.connector.Error as e:
        print("Gagal mengubah nama produk : {}".format(e))

def UpdateBerat(a, b):
    try:
        global Pass
        global Db
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=Pass,
            database=Db
        )
        myc = mydb.cursor()
        sql1 = "Update produk set berat = %s where nama = %s"
        val1 = (b, a)

        myc.execute(sql1, val1)
        mydb.commit()
        print("Berhasil mengubah berat produk!")
    except mysql.connector.Error as e:
        print("Gagal mengubah berat produk : {}".format(e))

def Menjual(a, b, c, d, e, f, g, h):
    try:
        global Pass
        global Db
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=Pass,
            database=Db
        )
        myc = mydb.cursor()
        sql = "Insert into produk values (null, %s, %s, %s, %s, %s, %s, %s)"
        val = (a, b, c, d, e, f, g)
        myc.execute(sql, val)
        mydb.commit()
        sql = "Select * from produk where nama = %s"
        val = (a, )
        myc.execute(sql, val)
        result = myc.fetchall()
        idprod = result[0][0]
        sql = "Insert into menjual values (%s, %s)"
        val = (h, idprod)
        myc.execute(sql, val)
        mydb.commit()
        print("Berhasil menambah produk!")
    except mysql.connector.Error as e:
        print("Gagal menambah produk : {}".format(e))

def HitungHarga(namaprod, jum, namakurir, berat):
    try:
        global Pass
        global Db
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=Pass,
            database=Db
        )
        mycursor = mydb.cursor()
        sql = "select * from kurir where nama = %s"
        val = (namakurir, )
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        hargakur = result[0][2]
        sql = "select * from produk where nama = %s"
        val = (namaprod, )
        mycursor.execute(sql, val)
        result1 = mycursor.fetchall()
        hargaprod = result1[0][2]
        hargatot = (hargakur*berat) + (hargaprod*jum)
        return int(hargatot)
    except mysql.connector.Error as e:
        print("Gagal menghitung harga produk : {}".format(e))

def Membeli(a, b, namapem, namakurir):
    try:
        global Pass
        global Db
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=Pass,
            database=Db
        )
        mycursor = mydb.cursor()
        sql = "Select * from produk where nama = %s"
        val = (a, )
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        temp = result[0][3]
        temp1 = result[0][0]
        berat = result[0][4]
        temp = (temp-b)
        sql = "Update produk set stok = %s where nama = %s"
        val = (temp, a)
        mycursor.execute(sql, val)
        mydb.commit()
        sql = "Select * from menjual where id = %s"
        val = (temp1, )
        mycursor.execute(sql, val)
        result1 = mycursor.fetchall()
        namapen = result1[0][0]
        sql = "Select * from kurir where nama = %s"
        val = (namakurir, )
        mycursor.execute(sql, val)
        result2 = mycursor.fetchall()
        idkurir = result2[0][0]
        harga = HitungHarga(a, b, namakurir, berat)
        sql = "Insert into transaksi values (null, %s, %s, %s, %s, %s, 'Diterima')"
        val = (namapem, namapen, temp1, idkurir, harga)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Berhasil membeli produk!")
        return harga
    except mysql.connector.Error as e:
        print("Gagal membeli produk : {}".format(e))


def SearchProduk(a):
    try:
        global Pass
        global Db
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=Pass,
            database=Db
        )
        mycursor = mydb.cursor()
        sql = "Select * from produk where nama like %s"
        val = (a + '%', )
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        return result
    except mysql.connector.Error as e:
        print("Gagal mencari produk : {}".format(e))

def SearchKategori(a):
    try:
        global Pass
        global Db
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=Pass,
            database=Db
        )
        mycursor = mydb.cursor()
        sql = "Select * from produk where kategori like %s"
        val = (a, )
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        return result
    except mysql.connector.Error as e:
        print("Gagal mencari produk : {}".format(e))

def AllKurir():
    try:
        global Pass
        global Db
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=Pass,
            database=Db
        )
        mycursor = mydb.cursor()
        mycursor.execute("Select * from kurir")
        result = mycursor.fetchall()
        return result
    except mysql.connector.Error as e:
        print("Gagal mencari kurir : {}".format(e))

def AllProduk():
    try:
        global Pass
        global Db
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=Pass,
            database=Db
        )
        mycursor = mydb.cursor()
        mycursor.execute("Select * from produk")
        result = mycursor.fetchall()
        return (result)
    except mysql.connector.Error as e:
        print("Gagal mencari produk : {}".format(e))

def AllJual(username):
    try:
        global Pass
        global Db
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=Pass,
            database=Db
        )
        mycursor = mydb.cursor()
        sql = "Select * from produk where id in (select id from menjual where username = %s)"
        val = (username, )
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        return result
    except mysql.connector.Error as e:
        print("Gagal mencari produk : {}".format(e))