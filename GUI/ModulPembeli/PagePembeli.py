from tkinter import *
import DefVar
import PageLogin
from PIL import ImageTk,Image
from ModulPembeli import showProduct, KategoriProduk, BerandaPembeli

def pagePembeli(frame):
    frame.destroy()
    menu = Frame(DefVar.root, bg=DefVar.background)
    menu.place(x=0, y=0, height=600, width=200)

    searchframe = Frame(DefVar.root, bg=DefVar.redcolor)
    searchframe.place(x=200, y=0, height=50, width=600)

    BerandaPembeli.berandaPembeli()

    DefVar.username = "Katara"

    #Search
    v = StringVar()
    search = Entry(searchframe, bd=1, bg=DefVar.white, relief=GROOVE, width=75, textvariable = v)
    search.place(x=50, y=25, anchor=W)
    searchtxt = Button(searchframe, text="Search", font="Helvetica 8", fg=DefVar.text, bg=DefVar.white, command=lambda:showProduct.showProduct(1, "Search", v.get()))
    searchtxt.place(x=510, y=25, anchor=W)

    #Foto Profil
    img = Image.open("../Foto/pengguna/katara.png")
    wImg, hImg = img.size
    if(wImg>hImg):
        hImg = hImg*95//wImg
        wImg = 95
    else:
        wImg = wImg*95//hImg
        hImg = 95
    img = img.resize((wImg, hImg), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(menu, image=img)
    panel.place(x=50,y=80)
    panel.img=img

    #Username
    username = Label(menu, text=DefVar.username, font="Helvetica 12 bold", fg=DefVar.white, bg=DefVar.background)
    username.place(x=70, y=200, anchor=W)

    beranda = Button(menu, text="Beranda", font= DefVar.font, activebackground=DefVar.redcolor, activeforeground=DefVar.white, fg=DefVar.white, bg=DefVar.background, padx=15, pady=5, relief=FLAT, width=10, command=BerandaPembeli.berandaPembeli)
    beranda.place(x=40, y=250, anchor=W)

    kategori = Button(menu, text="Kategori", font= DefVar.font, activebackground=DefVar.redcolor, activeforeground=DefVar.white, fg=DefVar.white, bg=DefVar.background, padx=15, pady=5, relief=FLAT, width=10, command=KategoriProduk.kategoriProduk)
    kategori.place(x=40, y=300, anchor=W)

    back = Button(menu, text="Back", font= "Helvetica 8", activebackground=DefVar.redcolor, activeforeground=DefVar.white, fg=DefVar.white, bg=DefVar.background, relief=FLAT, command=lambda:PageLogin.start(menu))
    back.place(x=10, y=20, anchor=W)