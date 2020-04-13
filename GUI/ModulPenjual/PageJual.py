from tkinter import *
from tkinter import filedialog
from pathlib import Path
import DefVar
from ModulFungsi.tes import *
from ModulPenjual import BerandaPenjual,SimpanProduk

def jualProduk():
    #Default
    x_txt = 100
    y_txt = 100
    x_entry = 200

    jualframe = Frame(DefVar.root, bg=DefVar.white)
    jualframe.place(x=200, y=0, height=600, width=600)

    #***************************************************************************************
    Produk = [0, "", 0, 0, 0, "", "", ""]
    #***************************************************************************************

    #Nama Produk
    namatxt = Label(jualframe, text="Nama Produk", font=DefVar.font, fg=DefVar.text, bg=DefVar.white)
    namatxt.place(x=x_txt, y=y_txt, anchor=W)
    vNama = StringVar()
    nama = Entry(jualframe, bd=1, bg=DefVar.white, relief=GROOVE, width=50, textvariable=vNama)
    nama.place(x=x_entry, y=y_txt, anchor=W)

    #Kategori
    kategoritxt = Label(jualframe, text="Kategori", font=DefVar.font, fg=DefVar.text, bg=DefVar.white)
    kategoritxt.place(x=x_txt, y=y_txt+50, anchor=W)
    var = StringVar(jualframe)
    var.set("")
    kategori = OptionMenu(jualframe, var, "Tuna Netra", "Tuna Wicara", "Tuna Rungu", "Tuna Daksa", "Tuna Grahita", command=lambda x=var.get():setKategori(x,Produk))
    kategori.config(bd=1, bg=DefVar.white, relief=GROOVE, width=20)
    kategori.place(x=x_entry, y=y_txt+50, anchor=W)
    
    #Harga
    hargatxt = Label(jualframe, text="Harga (Rp)", font=DefVar.font, fg=DefVar.text, bg=DefVar.white)
    hargatxt.place(x=x_txt, y=y_txt+100, anchor=W)
    harga = Spinbox(jualframe, bd=1, bg=DefVar.white, relief=GROOVE, from_=100, to=100000000000, width=24)
    harga.place(x=x_entry, y=y_txt+100, anchor=W)

    #Jumlah Barang
    stocktxt = Label(jualframe, text="Jumlah Barang", font=DefVar.font, fg=DefVar.text, bg=DefVar.white)
    stocktxt.place(x=x_txt, y=y_txt+150, anchor=W)
    stock = Spinbox(jualframe, bd=1, bg=DefVar.white, relief=GROOVE, from_=1, to=10000, width=15)
    stock.place(x=x_entry, y=y_txt+150, anchor=W)

    #Berat
    berattxt = Label(jualframe, text="Berat (kg)", font=DefVar.font, fg=DefVar.text, bg=DefVar.white)
    berattxt.place(x=x_txt+240, y=y_txt+150, anchor=W)
    berat = Spinbox(jualframe, bd=1, bg=DefVar.white, relief=GROOVE, from_=0, to=1000, width=12, increment=0.1)
    berat.place(x=x_entry+210, y=y_txt+150, anchor=W)

    #Spesifikasi
    spektxt = Label(jualframe, text="Spesifikasi", font=DefVar.font, fg=DefVar.text, bg=DefVar.white)
    spektxt.place(x=x_txt, y=y_txt+200, anchor=W)
    spek = Text(jualframe, bd=1, bg=DefVar.white, relief=GROOVE, height=10, width=37)
    spek.place(x=x_entry, y=y_txt+270, anchor=W)

    # #Picture
    picturetxt = Label(jualframe, text="Gambar", font=DefVar.font, fg=DefVar.text, bg=DefVar.white)
    picturetxt.place(x=x_txt, y=y_txt+390, anchor=W)
    vPicture = StringVar()
    picture = Entry(jualframe, bd=1, bg=DefVar.white, relief=GROOVE, width=35, textvariable=vPicture)
    picture.place(x=x_entry, y=y_txt+390, anchor=W)
    browse = Button(jualframe,text='Browse File',command=lambda:browseFile(picture), font="Helvetica 8", activebackground=DefVar.redcolor, activeforeground=DefVar.white, fg=DefVar.text, bg=DefVar.white, relief=GROOVE)
    browse.place(x=x_entry+235, y=y_txt+390, anchor=W)

    #Simpan
    simpan = Button(jualframe, text="Simpan", font=DefVar.font, activebackground=DefVar.white, activeforeground="#000000", fg=DefVar.white, bg=DefVar.redcolor, padx=15, pady=5, relief=FLAT, width=10, command=lambda: setEntry(vNama.get(), harga.get(), stock.get(), berat.get(), spek.get("1.0","end-1c"), vPicture.get(), Produk))
    simpan.place(x=x_entry+90, y=y_txt+450, anchor=W)

    #back
    back = Button(jualframe, text="Back", font= "Helvetica 8", activebackground=DefVar.redcolor, fg=DefVar.background, bg=DefVar.white, relief=FLAT, command=BerandaPenjual.BerandaPenjual)
    back.place(x=10, y=20, anchor=W)

def browseFile(picture):
    img_name = filedialog.askopenfilename(title = "Select A File", filetypes =(("jpeg files","*.jpg"),("png files","*.png")) )
    p = Path(img_name)

    list = p.parts

    hasil = list[len(list)-3]
    hasil += "/" + list[len(list)-2]
    hasil += "/" + list[len(list)-1]

    picture.delete(0,END)
    picture.insert(0,hasil)

def setEntry(nama, harga, stock, berat, spesifikasi, gambar, Produk):
    Produk[1] = nama
    Produk[2] = harga
    Produk[3] = stock
    Produk[4] = berat
    Produk[5] = spesifikasi
    Produk[6] = gambar
    saveProduct(Produk)
    SimpanProduk.simpanProduk()

def setKategori(a,Produk):
    Produk[7] = a

    #nama, harga, stok, berat, spek, image, kategori
def saveProduct(Produk):
    Menjual(Produk[1], Produk[2], Produk[3], Produk[4], Produk[5], Produk[6], Produk[7], DefVar.username)




