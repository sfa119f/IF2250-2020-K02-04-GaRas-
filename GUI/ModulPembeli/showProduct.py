from tkinter import *
import DefVar
from PIL import ImageTk,Image
#from ModulPembeli import KategoriProduk, BerandaPembeli

def showProduct(page, searchBy, Key):
    berandaframe = Frame(DefVar.root, bg=DefVar.white)
    berandaframe.place(x=200, y=50, height=550, width=600)

    #Contoh Data
    #Format : [Nama, Kategori, Harga, ImagePath]
    A = ["A", "KategoriA", 10000, "../Foto/produk/kacamata.png"]
    B = ["B", "KategoriA", 10000, "../Foto/produk/buku.jpg"]
    C = ["C", "KategoriA", 10000, "../Foto/produk/kacamata.png"]
    D = ["D", "KategoriD", 10000, "../Foto/produk/buku.jpg"]
    E = ["E", "KategoriE", 10000, "../Foto/produk/masker.jpg"]
    F = ["F", "KategoriF", 10000, "../Foto/produk/tongkat.png"]
    G = ["G", "KategoriG", 10000, "../Foto/produk/tongkat.png"]
    H = ["H", "KategoriH", 10000, "../Foto/produk/masker.jpg"]
    I = ["I", "KategoriI", 10000, "../Foto/produk/orthotic.png"]
    J = ["J", "KategoriJ", 10000, "../Foto/produk/tongkat.png"]
    K = ["K", "KategoriK", 10000, "../Foto/produk/masker.jpg"]
    L = ["L", "KategoriL", 10000, "../Foto/produk/orthotic.png"]
    M = ["M", "KategoriM", 10000, "../Foto/produk/buku.jpg"]
    N = ["N", "KategoriN", 10000, "../Foto/produk/masker.jpg"]
    O = ["O", "KategoriO", 10000, "../Foto/produk/tongkat.png"]
    P = ["P", "KategoriP", 10000, "../Foto/produk/kacamata.png"]
    Q = ["Q", "KategoriQ", 10000, "../Foto/produk/buku.jpg"]
    R = ["R", "KategoriR", 10000, "../Foto/produk/kacamata.png"]
    S = ["S", "KategoriS", 10000, "../Foto/produk/tongkat.png"]
    T = ["T", "KategoriT", 10000, "../Foto/produk/orthotic.png"]

    if(searchBy == "Search"):
        if(Key == "All"):
            List = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T]
        else:
            #Misal Key == "A"
            List = [A]           
    elif(searchBy == "Kategori"):
        #Key == "KategoriA"
        List = [A,B,C]  
        
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
            
            img = Image.open(Produk[3])
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
            nama = Label(frame1, text = Produk[0], bg=DefVar.white, font="Helvetica 8")
            nama.place(x=10, y=100)
            
            #Harga
            hargajual = str("Rp." + str(Produk[2]))
            harga = Label(frame1, text = hargajual, bg=DefVar.white, font="Helvetica 8")
            harga.place(x=10, y=115)

            #Button Beli
            jual = Button(frame1, text="Beli", font= "Helvetica 8", activebackground=DefVar.white, activeforeground=DefVar.text, fg=DefVar.white, bg=DefVar.redcolor, relief=FLAT)
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
        nextButton = Button(DefVar.root, text="Before", font="Helvetica 8", fg=DefVar.text, bg=DefVar.white, command=lambda:[showProduct(page-1,"Search","All"), drawPageLabel(page-1)])
        nextButton.place(x=220, y=570)
    
def drawPageLabel(page):
    pageLabel = Label(DefVar.root, text="page "+str(page), bg=DefVar.white, font="Helvetica 8")
    pageLabel.place(x=480, y=570)