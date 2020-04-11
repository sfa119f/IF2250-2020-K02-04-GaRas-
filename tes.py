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
        myc = mydb.cursor()

        sql = "Select * from produk where nama = %s"
        val = (a, )

        mycursor.execute(sql, val)

        result = mycursor.fetchall()

        temp = result[a][3]
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