import mysql.connector

def UpdateStok(a, b):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="XXX",
            database="YYY"
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
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="XXX",
            database="YYY"
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

def Membeli(a, b, namapem, namakurir):
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
        harga = (result2[0][2]*berat) + (harprod*b)
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
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="XXX",
            database="YYY"
        )
        mycursor = mydb.cursor()
        sql = "Select * from produk where nama like %s"
        val = (a + '%', )
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        a = 0
        for x in result:
            print("Nama produk :", result[a][1])
            print("Harga produk :", result[a][2])
            print("Stok produk :", result[a][3])
            print("Spesifikasi produk :", result[a][4])
            #print("Kategori produk : ", result[a][5])
            print()
            a+=1
    except mysql.connector.Error as e:
        print("Gagal mencari produk : {}".format(e))

def SearchKategori(a):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="XXX",
            database="YYY"
        )
        mycursor = mydb.cursor()
        sql = "Select * from produk where kategori like %s"
        val = (a, )
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        a = 0
        for x in result:
            print("Nama produk : ", result[a][1])
            print("Harga produk : ", result[a][2])
            print("Stok produk : ", result[a][3])
            print("Spesifikasi produk : ", result[a][4])
            #print("Kategori produk : ", result[a][5])
            print()
            a+=1
    except mysql.connector.Error as e:
        print("Gagal mencari produk : {}".format(e))


print("1. Mengupdate Stok")
print("2. Mengupdate Spek")
print("3. Mencari produk")
print("4. Mengupdate Harga")
print("5. Mengupdate Berat")
print("6. Mengupdate Nama")
print("7. Kategori Produk")
x = int(input("Masukkan pilihan menu : "))
if (x == 1):
    a = str(input("Masukkan nama produk : "))
    b = int(input("Masukkan jumlah produk : "))
    UpdateStok(a, b)
elif (x==2):
    a = str(input("Masukkan nama produk : "))
    b = str(input("Masukkan spek baru produk : "))
    UpdateSpek(a, b)
elif (x==3):
    a = str(input("Masukkan nama produk : "))
    print("Hasil pencarian : ")
    print()
    SearchProduk(a)
elif (x==4):
    a = str(input("Masukkan nama produk : "))
    b = str(input("Masukkan harga baru produk : "))
    UpdateHarga(a,b)
elif (x==5):
    a = str(input("Masukkan nama produk : "))
    b = str(input("Masukkan berat baru produk : "))
    UpdateBerat(a,b)
elif (x==6):
    a = str(input("Masukkan nama produk : "))
    b = str(input("Masukkan nama baru produk : "))
    UpdateNama(a,b)
elif (x==7):
    a = str(input("Masukkan kategori produk : "))
    print("Hasil pencarian : ")
    print()
    SearchKategori(a)
elif (x==8):
    a = str(input("Masukkan nama produk : "))
    b = str(input("Masukkan harga produk : "))
    c = str(input("Masukkan stok produk : "))
    d = str(input("Masukkan berat produk : "))
    e = str(input("Masukkan spesifikasi produk : "))
    f = str(input("Masukkan lokasi gambar produk : "))
    g = str(input("Masukkan kategori produk : "))
    Menjual(a, b, c, d, e, f, g)
elif (x==9):
    a = str(input("Masukkan nama produk : "))
    b = int(input("Masukkan jumlah produk : "))
    c = str(input("Masukkan nama pembeli : "))
    d = str(input("Masukkan nama jasa kurir : "))
    harga = Membeli(a,b,c,d)
    print(harga)