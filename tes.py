import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="1234",
  database="GaRas"
)

def UpdateStok(a, b):
    try:
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

def UpdateSpek()

a = str(input("Masukkan nama produk : "))
b = int(input("Masukkan jumlah produk : "))
UpdateStok(a, b)