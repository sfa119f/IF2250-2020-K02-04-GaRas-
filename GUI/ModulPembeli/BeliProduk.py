from tkinter import *
import DefVar
from PIL import ImageTk,Image
from ModulPembeli import BayarProduk, showProduct

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
    wImg, hImg = img.size
    if(wImg>hImg):
        hImg = hImg*270//wImg
        wImg = 270
    else:
        wImg = wImg*180//hImg
        hImg = 180
    img = img.resize((wImg, hImg), Image.ANTIALIAS)
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
    harga = showProduct.makeRp(str(Produk[2]))
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
    stocktxt.place(x=x_, y=y_ + 150)
    stock = Spinbox(frame, bd=1, bg=DefVar.white, relief=GROOVE, from_=1, to=Produk[3], width=30)
    stock.place(x=x_, y=y_ + 170)  

    #Pilihan Kurir
    kurirText = Label(frame, text="Ekspedisi Pengiriman", font="Helvetica 8", fg=DefVar.text, bg=DefVar.white)
    kurirText.place(x=x_ + 250, y=y_ + 200)

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
    var = StringVar(frame)
    opKurir = OptionMenu(frame, var, "JNE", "JNT", "SiCepat", "Tiki", command=lambda x=var.get():show(x, frame, listKurir, Produk, stock))
    opKurir.config(bd=1, bg=DefVar.white, relief=GROOVE, width=25)
    opKurir.place(x=x_, y=y_ + 220)

def show(value, frame, listKurir, Produk, stock):
    if(value == ""):
        value = ""
    else:
        if(value == "JNE"):
            Kurir = listKurir[0]
        elif(value=="JNT"):
            Kurir = listKurir[1]
        elif(value=="SiCepat"):
            Kurir = listKurir[2]
        elif(value=="Tiki"):
            Kurir = listKurir[3]

        #Label : Total Pembayaran
        totalpembayaran = Label(frame, text = "Total Pembayaran :", bg=DefVar.white, font="Helvetica 10")
        totalpembayaran.place(x=310, y=370)

        jmlBarang = int(stock.get())
        #-----------------------------------------------------------------------------------------------------
        #total = "Rp. " + str(HitungHarga(Produk[1], jmlBarang, Kurir[2], Produk[4]))
        #-----------------------------------------------------------------------------------------------------
        total = showProduct.makeRp(str(Produk[2]*jmlBarang + Kurir[2]*Produk[4]))    
        totalharga = Label(frame, text = total, bg=DefVar.white, font="Helvetica 15 bold", padx=20)
        totalharga.place(x=290, y=390)

        Bayar = Button(frame, text="Bayar", font=DefVar.font, activebackground=DefVar.white, activeforeground="#000000", fg=DefVar.white, bg=DefVar.redcolor, padx=15, pady=5, relief=FLAT, width=10, command=lambda:BayarProduk.bayarProduk(Produk, Kurir))
        Bayar.place(x=230, y=500, anchor=W)
