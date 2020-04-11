from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()

#Default
background = "#292728"
white = "#FFFFFF"
redcolor = "#b2081e"
text = "#000000"
size = "800x600+200+50"
title = "GaRas"
font = "Helvetica 10"

def pagepembeli(frame):
    frame.destroy()
    menu = Frame(root, bg=background)
    menu.place(x=0, y=0, height=600, width=200)

    searchframe = Frame(root, bg=redcolor)
    searchframe.place(x=200, y=0, height=50, width=600)

    #Search
    searchtxt = Button(searchframe, text="Search", font="Helvetica 8", fg=text, bg=white)
    searchtxt.place(x=510, y=25, anchor=W)
    search = Entry(searchframe, bd=1, bg=white, relief=GROOVE, width=75)
    search.place(x=50, y=25, anchor=W)

    berandaframe = Frame(root, bg=white)
    berandaframe.place(x=200, y=50, height=550, width=600)

    username = Label(menu, text="Arif Rahman", font="Helvetica 12 bold", fg=white, bg=background)
    username.place(x=50, y=200, anchor=W)

    beranda = Button(menu, text="Beranda", font= font, activebackground=redcolor, activeforeground=white, fg=white, bg=background, padx=15, pady=5, relief=FLAT, width=10)
    beranda.place(x=40, y=250, anchor=W)

    profil = Button(menu, text="Profil", font= font, activebackground=redcolor, activeforeground=white, fg=white, bg=background, padx=15, pady=5, relief=FLAT, width=10)
    profil.place(x=40, y=300, anchor=W)

    transaksi = Button(menu, text="Transaksi", font= font,activebackground=redcolor, activeforeground=white, fg=white, bg=background, padx=15, pady=5, relief=FLAT, width=10)
    transaksi.place(x=40, y=350, anchor=W)

    back = Button(menu, text="Back", font= "Helvetica 8", activebackground=redcolor, fg=white, bg=background, relief=FLAT, command=lambda:start(menu))
    back.place(x=10, y=20, anchor=W)

def pagepenjual(frame):
    frame.destroy()
    menu = Frame(root, bg=background)
    menu.place(x=0, y=0, height=600, width=200)

    berandaframe = Frame(root, bg=white)
    berandaframe.place(x=200, y=0, height=600, width=600)

    username = Label(menu, text="Arif Rahman", font="Helvetica 12 bold", bg=background, fg=white)
    username.place(x=50, y=200, anchor=W)

    beranda = Button(menu, text="Beranda", font= font, fg=white, activebackground=redcolor, bg=background, padx=15, pady=5, relief=FLAT, width=10)
    beranda.place(x=40, y=250, anchor=W)

    statistik = Button(menu, text="Statistik", font= font, activebackground=redcolor, fg=white, bg=background, padx=15, pady=5, relief=FLAT, width=10)
    statistik.place(x=40, y=300, anchor=W)

    transaksi = Button(menu, text="Transaksi", font= font, activebackground=redcolor, fg=white, bg=background, padx=15, pady=5, relief=FLAT, width=10)
    transaksi.place(x=40, y=350, anchor=W)

    jual = Button(menu, text="Jual", font= font, activebackground=redcolor, fg=white, bg=background, padx=15, pady=5, relief=FLAT, width=10, command=lambda:jualproduk(berandaframe))
    jual.place(x=40, y=400, anchor=W)

    back = Button(menu, text="Back", font= "Helvetica 8", activebackground=redcolor, fg=white, bg=background, relief=FLAT, command=lambda:start(menu))
    back.place(x=10, y=20, anchor=W)

def jualproduk(frame):
    frame.destroy()
    jualframe = Frame(root, bg=white)
    jualframe.place(x=200, y=0, height=600, width=600)
    #Default
    x_txt = 100
    y_txt = 100
    x_entry = 200

    #Nama Produk
    namatxt = Label(jualframe, text="Nama Produk", font=font, fg=text, bg=white)
    namatxt.place(x=x_txt, y=y_txt, anchor=W)
    nama = Entry(jualframe, bd=1, bg=white, relief=GROOVE, width=50)
    nama.place(x=x_entry, y=y_txt, anchor=W)


    #Kategori
    kategoritxt = Label(jualframe, text="Kategori", font=font, fg=text, bg=white)
    kategoritxt.place(x=x_txt, y=y_txt+50, anchor=W)
    kategori = Entry(jualframe, bd=1, bg=white, relief=GROOVE, width=50)
    kategori.place(x=x_entry, y=y_txt+50, anchor=W)
    
    #Harga
    hargatxt = Label(jualframe, text="Harga", font=font, fg=text, bg=white)
    hargatxt.place(x=x_txt, y=y_txt+100, anchor=W)
    harga = Entry(jualframe, bd=1, bg=white, relief=GROOVE, width=50)
    harga.place(x=x_entry, y=y_txt+100, anchor=W)

    #Jumlah Barang
    stocktxt = Label(jualframe, text="Jumlah Barang", font=font, fg=text, bg=white)
    stocktxt.place(x=x_txt, y=y_txt+150, anchor=W)
    stock = Spinbox(jualframe, bd=1, bg=white, relief=GROOVE, from_=1, to=10000, width=15)
    stock.place(x=x_entry, y=y_txt+150, anchor=W)

    #Berat
    berattxt = Label(jualframe, text="Berat", font=font, fg=text, bg=white)
    berattxt.place(x=x_txt+250, y=y_txt+150, anchor=W)
    berat = Entry(jualframe, bd=1, bg=white, relief=GROOVE, width=15)
    berat.place(x=x_entry+210, y=y_txt+150, anchor=W)

    #Spesifikasi
    spektxt = Label(jualframe, text="Spesifikasi", font=font, fg=text, bg=white)
    spektxt.place(x=x_txt, y=y_txt+200, anchor=W)
    spek = Text(jualframe, bd=1, bg=white, relief=GROOVE, height=10, width=37)
    spek.place(x=x_entry, y=y_txt+270, anchor=W)

    # #Picture
    picturetxt = Label(jualframe, text="Gambar", font=font, fg=text, bg=white)
    picturetxt.place(x=x_txt, y=y_txt+390, anchor=W)
    picture = Entry(jualframe, bd=1, bg=white, relief=GROOVE, width=35)
    picture.place(x=x_entry, y=y_txt+390, anchor=W)
    browse = Button(jualframe,text='Browse File',command=lambda:browse_file(picture), font="Helvetica 8", activebackground=redcolor, activeforeground=white, fg=text, bg=white, relief=GROOVE)
    browse.place(x=x_entry+235, y=y_txt+390, anchor=W)

    #Simpan
    penjual = Button(jualframe, text="Simpan", font=font, activebackground=white, activeforeground="#000000", fg=white, bg=redcolor, padx=15, pady=5, relief=FLAT, width=10)
    penjual.place(x=x_entry+90, y=y_txt+450, anchor=W)

def browse_file(picture):
    img_name = filedialog.askopenfilename(initialdir = "data/", title = "Select A File", filetypes =(("jpeg files","*.jpg"),) )
    img_name = img_name.split("data/")[-1]
    picture.delete(0,END)
    picture.insert(0,img_name)

def start(frame):
    frame.destroy()

    loginframe = Frame(root, bg=background)
    loginframe.place(x=0,y=0,height=600, width=800)
    welcome = Label(root, text="Selamat Datang di GaRas!", font="Helvetica 15 bold", bg=background, fg=white)
    login = Label(root, text="Masuk sebagai :", font="Helvetica 12", bg=background, fg=white)
    penjual = Button(root, text="Penjual", font=font, activebackground=background, fg=white, bg=redcolor, padx=15, pady=5, relief=FLAT, width=10, command=lambda:pagepenjual(loginframe))
    pembeli = Button(root, text="Pembeli", font=font, activebackground=background, fg=white, bg=redcolor, padx=15, pady=5, relief=FLAT, width=10, command=lambda:pagepembeli(loginframe))

    welcome.place(x=280,y=200, anchor = W)
    login.place(x=340, y=250, anchor = W)
    penjual.place(x=340, y=300, anchor = W)
    pembeli.place(x=340, y=350, anchor = W)

#----------------------[ MAIN ]--------------------------------------
root.title("GaRas")
root.geometry("800x600+200+50")
root.configure(background = background)

loginframe = Frame(root, bg=background)
loginframe.place(x=0,y=0,height=600, width=800)
welcome = Label(root, text="Selamat Datang di GaRas!", font="Helvetica 15 bold", bg=background, fg=white)
login = Label(root, text="Masuk sebagai :", font="Helvetica 12", bg=background, fg=white)
penjual = Button(root, text="Penjual", font=font, activebackground=background, fg=white, bg=redcolor, padx=15, pady=5, relief=FLAT, width=10, command=lambda:pagepenjual(loginframe))
pembeli = Button(root, text="Pembeli", font=font, activebackground=background, fg=white, bg=redcolor, padx=15, pady=5, relief=FLAT, width=10, command=lambda:pagepembeli(loginframe))

welcome.place(x=280,y=200, anchor = W)
login.place(x=340, y=250, anchor = W)
penjual.place(x=340, y=300, anchor = W)
pembeli.place(x=340, y=350, anchor = W)

root.mainloop()