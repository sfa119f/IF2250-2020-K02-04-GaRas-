from tkinter import *
import DefVar
from ModulPenjual import BerandaPenjual
from ModulFungsi.tes import *

def simpanProduk():
    frame = Frame(DefVar.root, bg=DefVar.white)
    frame.place(x=200, y=0, height=600, width=600)

    #Message
    var = StringVar()
    msg = Message(frame, textvariable=var, bg=DefVar.white, width = 540, relief=FLAT, font="Helvetica 30 bold", fg=DefVar.redcolor)
    var.set("Produk berhasil disimpan!")
    msg.place(x=30, y=200)

    #Button : Back
    back = Button(frame, text="Back", font= "Helvetica 8", activebackground=DefVar.redcolor, fg=DefVar.text, bg=DefVar.white, relief=FLAT, command=BerandaPenjual.BerandaPenjual)
    back.place(x=10, y=20, anchor=W)