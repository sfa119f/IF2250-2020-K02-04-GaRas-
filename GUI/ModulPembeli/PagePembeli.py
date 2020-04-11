from tkinter import *
import DefVar
import PageLogin
from ModulPembeli import showProduct

def pagePembeli(frame):
    frame.destroy()
    menu = Frame(DefVar.root, bg=DefVar.background)
    menu.place(x=0, y=0, height=600, width=200)

    searchframe = Frame(DefVar.root, bg=DefVar.redcolor)
    searchframe.place(x=200, y=0, height=50, width=600)

    berandaframe = Frame(DefVar.root, bg=DefVar.white)
    berandaframe.place(x=200, y=50, height=550, width=600)
    showProduct.showProduct("All")
    #Search
    searchtxt = Button(searchframe, text="Search", font="Helvetica 8", fg=DefVar.text, bg=DefVar.white)
    searchtxt.place(x=510, y=25, anchor=W)
    search = Entry(searchframe, bd=1, bg=DefVar.white, relief=GROOVE, width=75)
    search.place(x=50, y=25, anchor=W)

    username = Label(menu, text="Arif Rahman", font="Helvetica 12 bold", fg=DefVar.white, bg=DefVar.background)
    username.place(x=50, y=200, anchor=W)

    beranda = Button(menu, text="Beranda", font= DefVar.font, activebackground=DefVar.redcolor, activeforeground=DefVar.white, fg=DefVar.white, bg=DefVar.background, padx=15, pady=5, relief=FLAT, width=10)
    beranda.place(x=40, y=250, anchor=W)

    profil = Button(menu, text="Profil", font= DefVar.font, activebackground=DefVar.redcolor, activeforeground=DefVar.white, fg=DefVar.white, bg=DefVar.background, padx=15, pady=5, relief=FLAT, width=10)
    profil.place(x=40, y=300, anchor=W)

    transaksi = Button(menu, text="Transaksi", font= DefVar.font,activebackground=DefVar.redcolor, activeforeground=DefVar.white, fg=DefVar.white, bg=DefVar.background, padx=15, pady=5, relief=FLAT, width=10)
    transaksi.place(x=40, y=350, anchor=W)

    back = Button(menu, text="Back", font= "Helvetica 8", activebackground=DefVar.redcolor, fg=DefVar.white, bg=DefVar.background, relief=FLAT, command=lambda:PageLogin.start(menu))
    back.place(x=10, y=20, anchor=W)