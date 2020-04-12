from tkinter import *
import DefVar
from PIL import ImageTk,Image
from ModulPembeli import BeliProduk, PagePembeli
from ModulFungsi.tes import *

def showProduct(page, searchBy, Key):
    berandaframe = Frame(DefVar.root, bg=DefVar.white)
    berandaframe.place(x=200, y=50, height=550, width=600)

    #****************************************************************************************
    #Contoh Data
    #Format: Produk = [id(0), nama(1), harga(2), stock(3), berat(4), spek(5), image(6), kategori(7)]
    #A = [1, "A", 10000, 10, 1, "Spek", "../Foto/produk/kacamata.png", "KategoriA"]
    #B = [2, "B", 20000, 50, 1, "Spek", "../Foto/produk/buku.jpg", "KategoriA"]
    #C = [3, "C", 30000, 40, 1, "Spek", "../Foto/produk/kacamata.png","KategoriA"]
    #D = [4, "D", 40000, 30, 1, "Spek", "../Foto/produk/buku.jpg", "KategoriB"]
    #E = [5, "E", 30000, 10, 1, "Spek", "../Foto/produk/masker.jpg", "KategoriE"]
    #F = [6, "F", 20000, 50, 1, "Spek", "../Foto/produk/tongkat.png", "KategoriF"]
    #G = [7, "G", 20000, 10, 1, "Spek", "../Foto/produk/tongkat.png", "KategoriD"]
    #H = [8, "H", 10000, 20, 1, "Spek", "../Foto/produk/masker.jpg", "KategoriH"]
    #I = [9, "I", 10000, 10, 1, "Spek", "../Foto/produk/orthotic.png", "KategoriI"]
    #J = [10, "J", 10200, 20, 1, "Spek", "../Foto/produk/tongkat.png", "KategoriA"]
    #K = [11, "K", 30000, 11, 1, "Spek", "../Foto/produk/masker.jpg", "KategoriA"]
    #L = [12, "L", 10000, 12, 1, "Spek", "../Foto/produk/orthotic.png", "KategoriA"]
    #M = [13, "M", 10200, 11, 1, "Spek", "../Foto/produk/buku.jpg","KategoriA"]
    #N = [14, "N", 20000, 12, 1, "Spek", "../Foto/produk/masker.jpg","KategoriA"]
    #O = [15, "O", 20000, 13, 1, "Spek", "../Foto/produk/tongkat.png", "Kategori"]
    #P = [16, "P", 10000, 14, 1, "Spek", "../Foto/produk/kacamata.png", "Kategori"]
    #Q = [17, "Q", 10000, 13, 1, "Spek", "../Foto/produk/buku.jpg", "Kategori"]
    #R = [18, "R", 20000, 11, 1, "Spek", "../Foto/produk/kacamata.png","Kategori"]
    #S = [19, "S", 10000, 11, 1, "Spek", "../Foto/produk/tongkat.png", "Kategori"]
    #T = [20, "T", 90000, 15, 1, "Spek", "../Foto/produk/orthotic.png", "Kategori"]
    #***********************************************************************************************
    if(searchBy == "Search"):
        if(Key == "All"):
            #-------------------------------------------------------------
            List = AllProduk()
            #-------------------------------------------------------------
            #*************************************************************
            #List = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T]
            #*************************************************************
        else:
            #-------------------------------------------------------------
            List = SearchProduk(Key)
            #-------------------------------------------------------------
            #*************************************************************
            #List = [A]
            #*************************************************************           
    else:
        #-----------------------------------------------------------------
        List = SearchKategori(Key)
        #-----------------------------------------------------------------
        #*****************************************************************
        #List = [A,B,C]  
        #*****************************************************************
 
        
    x_ = 0
    y_ = 0
    a = 0
    i = page*9-9
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
            hargajual = makeRp(str(Produk[2]))
            harga = Label(frame1, text = hargajual, bg=DefVar.white, font="Helvetica 8")
            harga.place(x=10, y=115)

            #Button Beli
            jual = Button(frame1, text="Beli", font= "Helvetica 8", activebackground=DefVar.white, activeforeground=DefVar.text, fg=DefVar.white, bg=DefVar.redcolor, relief=FLAT, command=lambda a = Produk[1] : BeliProduk.beliProduk(a))
            jual.place(x=10, y=150, anchor=W)

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
        nextButton = Button(DefVar.root, text="Previous", font="Helvetica 8", fg=DefVar.text, bg=DefVar.white, command=lambda:[showProduct(page-1,"Search","All"), drawPageLabel(page-1)])
        nextButton.place(x=220, y=570)
    
def drawPageLabel(page):
    pageLabel = Label(DefVar.root, text="page "+str(page), bg=DefVar.white, font="Helvetica 8")
    pageLabel.place(x=480, y=570)

def makeRp(uang):
    hasil = "Rp. "
    if(len(str(uang))%3 == 0):
        i = 0
    else:
        if(len(str(uang))%3 == 1):
            hasil += str(uang[0]) + "."
            i = 1
        elif(len(str(uang))%3 == 2):
            hasil += str(uang[0]) + str(uang[1]) + "."
            i = 2            

    while(i < len(str(uang))):
        a = 0
        while(a < 3 and i < len(str(uang))):
            hasil += str(uang[i])
            i += 1
            a += 1
        if(i < len(str(uang))): hasil += "."
        a = 0
    return hasil