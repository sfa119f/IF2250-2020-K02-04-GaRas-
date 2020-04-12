from tkinter import *
import DefVar
from ModulPembeli import BerandaPembeli

def bayarProduk(Produk, Kurir):
    frame = Frame(DefVar.root, bg=DefVar.white)
    frame.place(x=200, y=50, height=550, width=600)

    #------------------------------------------------------------------
    #Membeli(namaProduk, jmlBarang, DefVar.username, namaKurir)
    #------------------------------------------------------------------

    #Message
    var = StringVar()
    msg = Message(frame, textvariable=var, bg=DefVar.white, width = 540, relief=FLAT, font="Helvetica 50 bold", fg=DefVar.redcolor)
    var.set("Transaksi Berhasil")
    msg.place(x=100, y=100)
    
    #Button : Back
    back = Button(frame, text="Back", font= "Helvetica 8", activebackground=DefVar.redcolor, fg=DefVar.text, bg=DefVar.white, relief=FLAT, command=BerandaPembeli.berandaPembeli)
    back.place(x=10, y=20, anchor=W)