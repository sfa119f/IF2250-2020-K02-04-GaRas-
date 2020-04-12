from tkinter import *
import DefVar
from ModulPembeli import KategoriProduk, BerandaPembeli

def showProduct(searchBy, Key):
    berandaframe = Frame(DefVar.root, bg=DefVar.white)
    berandaframe.place(x=200, y=50, height=550, width=600)

    #Contoh Data
    A = ["A", "KategoriA", 10000, 10, 1, "Blablabla", "Foto/pengguna/Aang.jpg"]
    B = ["B", "KategoriA", 10000, 10, 1, "Blablabla", "Foto/pengguna/Aang.jpg"]
    C = ["C", "KategoriA", 10000, 10, 1, "Blablabla", "Foto/pengguna/Aang.jpg"]
    D = ["D", "KategoriD", 10000, 10, 1, "Blablabla", "Foto/pengguna/Aang.jpg"]
    E = ["E", "KategoriE", 10000, 10, 1, "Blablabla", "Foto/pengguna/Aang.jpg"]
    F = ["F", "KategoriF", 10000, 10, 1, "Blablabla", "Foto/pengguna/Aang.jpg"]
    G = ["G", "KategoriG", 10000, 10, 1, "Blablabla", "Foto/pengguna/Aang.jpg"]
    H = ["H", "KategoriH", 10000, 10, 1, "Blablabla", "Foto/pengguna/Aang.jpg"]
    I = ["I", "KategoriI", 10000, 10, 1, "Blablabla", "Foto/pengguna/Aang.jpg"]

    if(searchBy == "Search"):
        if(Key == "All"):
            List = [A,B,C,D,E,F,G,H,I]

        else:
            #Misal Key == "A"
            List = [A]

            #Button : Back
            back = Button(berandaframe, text="Back", font= "Helvetica 8", activebackground=DefVar.redcolor, fg=DefVar.background, bg=DefVar.white, relief=FLAT, command=BerandaPembeli.berandaPembeli)
            back.place(x=10, y=20, anchor=W)
                       
    elif(searchBy == "Kategori"):
        #Key == "KategoriA"
        List = [A,B,C] 

        #Button : Back
        back = Button(berandaframe, text="Back", font= "Helvetica 8", activebackground=DefVar.redcolor, fg=DefVar.background, bg=DefVar.white, relief=FLAT, command=KategoriProduk.kategoriProduk)
        back.place(x=10, y=20, anchor=W) 
        
    x_ = 0
    y_ = 0
    a = 0
    i = 0
    while(i<len(List)):
        a = 0
        while(a<3 and i<len(List)):
            Produk = List[i]

            frame1 = Frame(berandaframe, bg=DefVar.white)
            frame1.place(x=x_, y=y_, width=200, height=170)
            
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

            #Picturenya belom bisa :(
            x_ += 200
            a += 1
            i += 1

        x_ = 0
        y_ += 180