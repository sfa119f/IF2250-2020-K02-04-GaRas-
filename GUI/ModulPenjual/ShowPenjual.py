from tkinter import *
import DefVar
from PIL import ImageTk,Image
from ModulPembeli import showProduct
from ModulFungsi.tes import *

def ShowPenjual(page):
    berandaframe = Frame(DefVar.root, bg=DefVar.white)
    berandaframe.place(x=200, y=50, height=550, width=600)

    x_ = 0
    y_ = 0
    a = 0
    i = page*9-9
    List = AllJual(DefVar.username)
    while(i<len(List) and i<page*9):
        a = 0
        while(a<3 and i<len(List) and i<page*9):
            Produk = List[i]

            frame1 = Frame(berandaframe, bg=DefVar.white)
            frame1.place(x=x_, y=y_, width=200, height=160)
            filename = "../" + Produk[6]
            img = Image.open(filename)
            wImg, hImg = img.size
            if(wImg>hImg):
                hImg = hImg*130//wImg
                wImg = 130
            else:
                wImg = wImg*85//hImg
                hImg = 85
            img = img.resize((wImg, hImg), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = Label(frame1, image=img)
            panel.place(x=10,y=10)
            panel.img=img

            #Nama
            nama = Label(frame1, text = Produk[1], bg=DefVar.white, font="Helvetica 8")
            nama.place(x=10, y=100)
            
            #Harga
            hargajual = showProduct.makeRp(str(Produk[2]))
            harga = Label(frame1, text = hargajual, bg=DefVar.white, font="Helvetica 8")
            harga.place(x=10, y=115)

            x_ += 200
            a += 1
            i += 1

        x_ = 0
        y_ += 180

    drawPageLabel(page)

    if(len(List)>=page*9):
        nextButton = Button(DefVar.root, text="Next", font="Helvetica 8", fg=DefVar.text, bg=DefVar.white, command=lambda:[showProduct(page+1,"Search","All"), drawPageLabel(page+1)])
        nextButton.place(x=750, y=570)
    
    if(page!=1):
        nextButton = Button(DefVar.root, text="Before", font="Helvetica 8", fg=DefVar.text, bg=DefVar.white, command=lambda:[showProduct(page-1,"Search","All"), drawPageLabel(page-1)])
        nextButton.place(x=220, y=570)
    
def drawPageLabel(page):
    pageLabel = Label(DefVar.root, text="page "+str(page), bg=DefVar.white, font="Helvetica 8")
    pageLabel.place(x=480, y=570)