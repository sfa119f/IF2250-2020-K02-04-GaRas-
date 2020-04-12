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