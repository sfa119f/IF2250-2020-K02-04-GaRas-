from tkinter import *
import DefVar
import PageLogin
from ModulPenjual import PageJual 

def pagePenjual(frame):
    frame.destroy()
    menu = Frame(DefVar.root, bg=DefVar.background)
    menu.place(x=0, y=0, height=600, width=200)

    berandaframe = Frame(DefVar.root, bg=DefVar.white)
    berandaframe.place(x=200, y=0, height=600, width=600)

    username = Label(menu, text="Arif Rahman", font="Helvetica 12 bold", bg=DefVar.background, fg=DefVar.white)
    username.place(x=50, y=200, anchor=W)

    beranda = Button(menu, text="Beranda", font= DefVar.font, fg=DefVar.white, activebackground=DefVar.redcolor, bg=DefVar.background, padx=15, pady=5, relief=FLAT, width=10)
    beranda.place(x=40, y=250, anchor=W)

    statistik = Button(menu, text="Statistik", font= DefVar.font, activebackground=DefVar.redcolor, fg=DefVar.white, bg=DefVar.background, padx=15, pady=5, relief=FLAT, width=10)
    statistik.place(x=40, y=300, anchor=W)

    transaksi = Button(menu, text="Transaksi", font= DefVar.font, activebackground=DefVar.redcolor, fg=DefVar.white, bg=DefVar.background, padx=15, pady=5, relief=FLAT, width=10)
    transaksi.place(x=40, y=350, anchor=W)

    jual = Button(menu, text="Jual", font= DefVar.font, activebackground=DefVar.redcolor, fg=DefVar.white, bg=DefVar.background, padx=15, pady=5, relief=FLAT, width=10, command=PageJual.jualProduk)
    jual.place(x=40, y=400, anchor=W)

    back = Button(menu, text="Back", font= "Helvetica 8", activebackground=DefVar.redcolor, fg=DefVar.white, bg=DefVar.background, relief=FLAT, command=lambda:PageLogin.start(menu))
    back.place(x=10, y=20, anchor=W)