from tkinter import *
import DefVar
from ModulPembeli import showProduct, BerandaPembeli

def kategoriProduk():
    frame = Frame(DefVar.root, bg=DefVar.white)
    frame.place(x=200, y=50, height=550, width=600)

    #Label : Cari Berdasarkan Kategori
    Judul = Label(frame, text = "Cari berdasarkan Kategori : ", bg=DefVar.white, font="Helvetica 12 bold")
    Judul.place(x=10, y=100)

    #Button : Tuna Netra
    netra = Button(frame, text="Tuna Netra", font=DefVar.font, activebackground=DefVar.white, activeforeground="#000000", fg=DefVar.white, bg=DefVar.redcolor, padx=100, pady=5, relief=FLAT, width=10, command=lambda:showProduct.showProduct(1, "Kategori","Tuna Netra"))
    netra.place(x=150, y=150, anchor=W)

    #Button : Tuna Rungu
    rungu = Button(frame, text="Tuna Rungu", font=DefVar.font, activebackground=DefVar.white, activeforeground="#000000", fg=DefVar.white, bg=DefVar.redcolor, padx=100, pady=5, relief=FLAT, width=10, command=lambda:showProduct.showProduct(1, "Kategori","Tuna Rungu"))
    rungu.place(x=150, y=200, anchor=W)

    #Button : Tuna Wicara
    wicara = Button(frame, text="Tuna Wicara", font=DefVar.font, activebackground=DefVar.white, activeforeground="#000000", fg=DefVar.white, bg=DefVar.redcolor, padx=100, pady=5, relief=FLAT, width=10, command=lambda:showProduct.showProduct(1, "Kategori","Tuna Wicara"))
    wicara.place(x=150, y=250, anchor=W)

    #Button : Tuna Daksa
    daksa = Button(frame, text="Tuna Daksa", font=DefVar.font, activebackground=DefVar.white, activeforeground="#000000", fg=DefVar.white, bg=DefVar.redcolor, padx=100, pady=5, relief=FLAT, width=10, command=lambda:showProduct.showProduct(1, "Kategori","Tuna Daksa"))
    daksa.place(x=150, y=300, anchor=W)

    #Button : Tuna Grahita
    grahita = Button(frame, text="Tuna Grahita", font=DefVar.font, activebackground=DefVar.white, activeforeground="#000000", fg=DefVar.white, bg=DefVar.redcolor, padx=100, pady=5, relief=FLAT, width=10, command=lambda:showProduct.showProduct(1, "Kategori","Tuna Grahita"))
    grahita.place(x=150, y=350, anchor=W)

    #Button : Back
    back = Button(frame, text="Back", font= "Helvetica 8", activebackground=DefVar.redcolor, fg=DefVar.background, bg=DefVar.white, relief=FLAT, command=BerandaPembeli.berandaPembeli)
    back.place(x=10, y=20, anchor=W)