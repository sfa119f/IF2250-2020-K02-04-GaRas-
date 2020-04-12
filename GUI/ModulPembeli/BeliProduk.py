from tkinter import *
import DefVar
from PIL import ImageTk,Image
from ModulPembeli import BayarProduk

def beliProduk(NamaProduk):
    frame = Frame(DefVar.root, bg=DefVar.white)
    frame.place(x=200, y=50, height=550, width=600)

    x_ = 20
    y_ = 200
    #------------------------------------------------
    #List = SearchProduk(NamaProduk)
    #Produk = List[0]
    #------------------------------------------------
    
    #************************************************
    #Format: Produk = [id, nama, harga, stock, berat, spek, image, kategori]
    Produk = [101, NamaProduk, 1000, 10, 10, "Desc", "../Foto/produk/buku.jpg", "Buku"]
    #*************************************************

    #Foto Produk
    img = Image.open(Produk[6])
    img = img.resize((270,180), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(frame, image=img)
    panel.place(x=150,y=10)
    panel.img=img
    #Label : Nama Produk
    nama = Label(frame, text = Produk[1], bg=DefVar.white, font="Helvetica 15 bold")
    nama.place(x=x_, y=y_)

    #Label : Tersedia
    tersedia = "Tersedia : " + str(Produk[3]) + " Produk"
    stock = Label(frame, text = tersedia, bg=DefVar.white, font="Helvetica 8", fg=DefVar.redcolor)
    stock.place(x=x_, y=y_ + 30)

    #Label : Harga
    harga = "Rp. " + str(Produk[2])
    price = Label(frame, text = harga, bg=DefVar.white, font="Helvetica 12")
    price.place(x=x_, y=y_ + 50)

    #Label : Deskripsi
    deskripsi = Label(frame, text = "Deskripsi Produk", bg=DefVar.white, font="Helvetica 10")
    deskripsi.place(x=x_, y=y_ + 90)

    #Message : Deskripsi
    var = StringVar()
    desc = Message(frame, textvariable=var, bg=DefVar.white, width = 540, relief=FLAT, font="Helvetica 8")
    var.set(Produk[5])
    desc.place(x=x_, y=y_ + 110)

    #Jumlah Pembelian
    stocktxt = Label(frame, text="Jumlah Pembelian", font="Helvetica 8", fg=DefVar.text, bg=DefVar.white)
    stocktxt.place(x=x_, y=y_ + 180)
    stock = Spinbox(frame, bd=1, bg=DefVar.white, relief=GROOVE, from_=1, to=Produk[3], width=30)
    stock.place(x=x_, y=y_ + 200)  

    #Pilihan Kurir
    kurirText = Label(frame, text="Ekspedisi Pengiriman", font="Helvetica 8", fg=DefVar.text, bg=DefVar.white)
    kurirText.place(x=x_ + 250, y=y_ + 180)

    #Daftar Kurir
    menuKurir = Menubutton(frame, text="", relief=GROOVE, bg=DefVar.white, font="Helvetica 8", fg="grey", width=30)
    menuKurir.place(x=x_ + 250, y=y_ + 200)
    menuKurir.menu = Menu(menuKurir, tearoff=0)
    menuKurir["menu"] = menuKurir.menu

    #--------------------------------------------------------
    #listKurir = AllKurir()
    #--------------------------------------------------------

    #********************************************************
    #Format: Kurir = [id, nama, harga, alamat, image]
    Kurir1 = ["1", "JNE", 10000, "", ""]
    Kurir2 = ["2", "JNT", 20000, "", ""]
    Kurir3 = ["3", "SiCepat", 30000, "", ""]
    Kurir4 = ["4", "Tiki", 40000, "", ""]

    #listnya dimasukin list
    listKurir = [Kurir1, Kurir2, Kurir3, Kurir4]
    #********************************************************
    
    for i in range(len(listKurir)):
        Kurir = listKurir[i]
        menuKurir.menu.add_command(label=Kurir[1], command=lambda x=Kurir : showTotal(frame, menuKurir, listKurir, x, Produk, stock))



def showTotal(frame, menuKurir, listKurir, Kurir, Produk, stock):
    menuKurir.destroy()
    jmlBarang = int(stock.get())

    #Ganti text menubutton
    menuKurir = Menubutton(frame, text=Kurir[1], relief=GROOVE, bg=DefVar.white, font="Helvetica 8", fg="grey", width=30)
    menuKurir.place(x=270, y=400)
    menuKurir.menu = Menu(menuKurir, tearoff=0)
    menuKurir["menu"] = menuKurir.menu

    for i in range(len(listKurir)):
        Kurir = listKurir[i]
        menuKurir.menu.add_command(label=Kurir[1], command=lambda x=Kurir : showTotal(frame, menuKurir, listKurir, x, Produk, stock))

    #Label : Total Pembayaran
    totalpembayaran = Label(frame, text = "Total Pembayaran : ", bg=DefVar.white, font="Helvetica 10")
    totalpembayaran.place(x=20, y=430)

    #-----------------------------------------------------------------------------------------------------
    #total = "Rp. " + str(HitungHarga(Produk[1], jmlBarang, Kurir[2], Produk[4]))
    #-----------------------------------------------------------------------------------------------------

    #*****************************************************************************************************
    #Label : Rp.
    total = "Rp. " + str(Produk[2]*jmlBarang + Kurir[2]*Produk[4])    
    #*****************************************************************************************************
    totalharga = Label(frame, text = total, bg=DefVar.white, font="Helvetica 12 bold", padx=20)
    totalharga.place(x=20, y=450)

    #Button : Bayar
    Bayar = Button(frame, text="Bayar", font=DefVar.font, activebackground=DefVar.white, activeforeground="#000000", fg=DefVar.white, bg=DefVar.redcolor, padx=15, pady=5, relief=FLAT, width=10, command=lambda:BayarProduk.bayarProduk(Produk, Kurir))
    Bayar.place(x=230, y=500, anchor=W)