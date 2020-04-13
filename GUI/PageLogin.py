from tkinter import *
import DefVar
from ModulPenjual import PagePenjual
from ModulPembeli import PagePembeli

def start(frame):
    frame.destroy()

    loginframe = Frame(DefVar.root, bg=DefVar.background)
    loginframe.place(x=0,y=0,height=600, width=800)

    welcome = Label(DefVar.root, text="Selamat Datang di GaRas!", font="Helvetica 15 bold", bg=DefVar.background, fg=DefVar.white)

    login = Label(DefVar.root, text="Masuk sebagai :", font="Helvetica 12", bg=DefVar.background, fg=DefVar.white)

    penjual = Button(DefVar.root, text="Penjual", font=DefVar.font, activebackground=DefVar.background, fg=DefVar.white, bg=DefVar.redcolor, padx=15, pady=5, relief=FLAT, width=10, command=lambda:PagePenjual.pagePenjual(loginframe))

    pembeli = Button(DefVar.root, text="Pembeli", font=DefVar.font, activebackground=DefVar.background, fg=DefVar.white, bg=DefVar.redcolor, padx=15, pady=5, relief=FLAT, width=10, command=lambda:PagePembeli.pagePembeli(loginframe))

    welcome.place(x=280,y=200, anchor = W)
    login.place(x=340, y=250, anchor = W)
    penjual.place(x=340, y=300, anchor = W)
    pembeli.place(x=340, y=350, anchor = W)