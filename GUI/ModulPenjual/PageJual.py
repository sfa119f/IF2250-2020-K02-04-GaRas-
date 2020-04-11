from tkinter import *
from tkinter import filedialog
import DefVar

def jualProduk(frame):
    #Default
    x_txt = 100
    y_txt = 100
    x_entry = 200

    frame.destroy()
    jualframe = Frame(DefVar.root, bg=DefVar.white)
    jualframe.place(x=200, y=0, height=600, width=600)

    #Nama Produk
    namatxt = Label(jualframe, text="Nama Produk", font=DefVar.font, fg=DefVar.text, bg=DefVar.white)
    namatxt.place(x=x_txt, y=y_txt, anchor=W)
    nama = Entry(jualframe, bd=1, bg=DefVar.white, relief=GROOVE, width=50)
    nama.place(x=x_entry, y=y_txt, anchor=W)


    #Kategori
    kategoritxt = Label(jualframe, text="Kategori", font=DefVar.font, fg=DefVar.text, bg=DefVar.white)
    kategoritxt.place(x=x_txt, y=y_txt+50, anchor=W)
    kategori = Entry(jualframe, bd=1, bg=DefVar.white, relief=GROOVE, width=50)
    kategori.place(x=x_entry, y=y_txt+50, anchor=W)
    
    #Harga
    hargatxt = Label(jualframe, text="Harga", font=DefVar.font, fg=DefVar.text, bg=DefVar.white)
    hargatxt.place(x=x_txt, y=y_txt+100, anchor=W)
    harga = Entry(jualframe, bd=1, bg=DefVar.white, relief=GROOVE, width=50)
    harga.place(x=x_entry, y=y_txt+100, anchor=W)

    #Jumlah Barang
    stocktxt = Label(jualframe, text="Jumlah Barang", font=DefVar.font, fg=DefVar.text, bg=DefVar.white)
    stocktxt.place(x=x_txt, y=y_txt+150, anchor=W)
    stock = Spinbox(jualframe, bd=1, bg=DefVar.white, relief=GROOVE, from_=1, to=10000, width=15)
    stock.place(x=x_entry, y=y_txt+150, anchor=W)

    #Berat
    berattxt = Label(jualframe, text="Berat", font=DefVar.font, fg=DefVar.text, bg=DefVar.white)
    berattxt.place(x=x_txt+250, y=y_txt+150, anchor=W)
    berat = Entry(jualframe, bd=1, bg=DefVar.white, relief=GROOVE, width=15)
    berat.place(x=x_entry+210, y=y_txt+150, anchor=W)

    #Spesifikasi
    spektxt = Label(jualframe, text="Spesifikasi", font=DefVar.font, fg=DefVar.text, bg=DefVar.white)
    spektxt.place(x=x_txt, y=y_txt+200, anchor=W)
    spek = Text(jualframe, bd=1, bg=DefVar.white, relief=GROOVE, height=10, width=37)
    spek.place(x=x_entry, y=y_txt+270, anchor=W)

    # #Picture
    picturetxt = Label(jualframe, text="Gambar", font=DefVar.font, fg=DefVar.text, bg=DefVar.white)
    picturetxt.place(x=x_txt, y=y_txt+390, anchor=W)
    picture = Entry(jualframe, bd=1, bg=DefVar.white, relief=GROOVE, width=35)
    picture.place(x=x_entry, y=y_txt+390, anchor=W)
    browse = Button(jualframe,text='Browse File',command=lambda:browseFile(picture), font="Helvetica 8", activebackground=DefVar.redcolor, activeforeground=DefVar.white, fg=DefVar.text, bg=DefVar.white, relief=GROOVE)
    browse.place(x=x_entry+235, y=y_txt+390, anchor=W)

    #Simpan
    penjual = Button(jualframe, text="Simpan", font=DefVar.font, activebackground=DefVar.white, activeforeground="#000000", fg=DefVar.white, bg=DefVar.redcolor, padx=15, pady=5, relief=FLAT, width=10)
    penjual.place(x=x_entry+90, y=y_txt+450, anchor=W)

def browseFile(picture):
    img_name = filedialog.askopenfilename(initialdir = "data/", title = "Select A File", filetypes =(("jpeg files","*.jpg"),) )
    img_name = img_name.split("data/")[-1]
    picture.delete(0,END)
    picture.insert(0,img_name)