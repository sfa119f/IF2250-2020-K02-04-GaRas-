import mysql.connector

def UpdateStok(a, b):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="1234",
            database="GaRas"
        )
        mycursor = mydb.cursor()
        myc = mydb.cursor()

        sql = "Select * from produk where nama = %s"
        val = (a, )

        mycursor.execute(sql, val)

        result = mycursor.fetchall()

        temp = result[0][3]
        print (temp)

        temp = temp-b

        sql1 = "Update produk set stok = %s where nama = %s"
        val1 = (temp, a)

        myc.execute(sql1, val1)
        mydb.commit()
        print("Berhasil mengubah stok produk!")
    except mysql.connector.Error as e:
        print("Gagal mengubah stok produk : {}".format(e))

def UpdateSpek(a, b):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="1234",
            database="GaRas"
        )
        myc = mydb.cursor()
        sql1 = "Update produk set spek = %s where nama = %s"
        val1 = (b, a)

        myc.execute(sql1, val1)
        mydb.commit()
        print("Berhasil mengubah spek produk!")
    except mysql.connector.Error as e:
        print("Gagal mengubah spek produk : {}".format(e))

<<<<<<< Updated upstream
=======
def UpdateHarga(a, b):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="XXX",
            database="YYY"
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
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="XXX",
            database="YYY"
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
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="XXX",
            database="YYY"
        )
        myc = mydb.cursor()
        sql1 = "Update produk set berat = %s where nama = %s"
        val1 = (b, a)

        myc.execute(sql1, val1)
        mydb.commit()
        print("Berhasil mengubah berat produk!")
    except mysql.connector.Error as e:
        print("Gagal mengubah berat produk : {}".format(e))

def Menjual(a, b, c, d, e, f, g):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="XXX",
            database="YYY"
        )
        myc = mydb.cursor()
        sql = "Insert into produk values (null, %s, %s, %s, %s, %s, %s, %s)"
        val = (a, b, c, d, e, f, g)

        myc.execute(sql, val)
        mydb.commit()
        print("Berhasil menambah produk!")
    except mysql.connector.Error as e:
        print("Gagal menambah produk : {}".format(e))

def Membeli(a, b, namapem, idkurir):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="XXX",
            database="YYY"
        )
        mycursor = mydb.cursor()
        sql = "Select * from produk where nama = %s"
        val = (a, )
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        temp = result[0][3]
        temp1 = result[0][0]
        harprod = result[0][2]
        berat = result[0][4]
        temp = temp-b
        sql = "Update produk set stok = %s where nama = %s"
        val = (temp, a)
        mycursor.execute(sql, val)
        mydb.commit()
        sql = "Select * from menjual where id = %s"
        val = (temp1, )
        result1 = mycursor.fetchall()
        namapen = result1[0][0]
        sql = "Select * from kurir where id = %s"
        val = (idkurir, )
        mycursor.execute(sql, val)
        result2 = mycursor.fetchall()
        harga = (result2[0][2]*berat) + harprod
        sql = "Insert into transaksi values (null, %s, %s, %s, %s, %s, 'Diterima')"
        val = (namapem, namapen, temp1, idkurir, harga)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Berhasil membeli produk!")
    except mysql.connector.Error as e:
        print("Gagal membeli produk : {}".format(e))

>>>>>>> Stashed changes
def SearchProduk(a):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="1234",
            database="GaRas"
        )
        mycursor = mydb.cursor()
        sql = "Select * from produk where nama like %s"
        val = ('%' + a + '%', )
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        for x in range(len(result)):
            print("Nama produk : ", result[x][1])
            print("Harga produk : ", result[x][2])
            print("Stok produk : ", result[x][3])
            print("Spesifikasi produk : ", result[x][4])
            print("Kategori produk : ", result[x][5])
            print()
    except mysql.connector.Error as e:
        print("Gagal mencari produk : {}".format(e))

def SearchKategori(a):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="1234",
            database="GaRas"
        )
        mycursor = mydb.cursor()
        sql = "Select * from produk where kategori like %s"
        val = (a, )
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        for x in range(len(result)):
            print("Nama produk : ", result[x][1])
            print("Harga produk : ", result[x][2])
            print("Stok produk : ", result[x][3])
            print("Spesifikasi produk : ", result[x][4])
            print("Kategori produk : ", result[x][5])
            print()
    except mysql.connector.Error as e:
        print("Gagal mencari produk : {}".format(e))




print("1. Mengupdate Stok")
print("2. Mengupdate Spek")
print("3. Mencari produk")
print("4. Mencari produk berdasarkan kategori")
print("5. Menambahkan produk yang dijual")
x = int(input("Masukkan pilihan menu : "))
if (x == 1):
    a = str(input("Masukkan nama produk : "))
    b = int(input("Masukkan jumlah produk : "))
    UpdateStok(a, b)
elif (x==2):
    a = str(input("Masukkan nama produk : "))
    b = str(input("Masukkan spek produk : "))
    UpdateSpek(a, b)
elif (x==3):
    a = str(input("Masukkan nama produk : "))
    print("Hasil pencarian : ")
    print()
    SearchProduk(a)
elif (x==4):
    a = str(input("Masukkan kategori produk : "))
    print("Hasil pencarian : ")
    print()
    SearchKategori(a)
"""elif (x==5):
    a = str(input("Masukkan nama produk : "))
    b = int(input("Masukkan harga produk : "))
    c = int(input("Masukkan stok produk : "))
    d = str(input("Masukkan spesifikasi produk : "))
    e = str(input("Masukkan lokasi gambar produk : "))
    f = str(input("Masukkan kategori produk : "))
    Menjual(a, b, c, d, e, f)"""