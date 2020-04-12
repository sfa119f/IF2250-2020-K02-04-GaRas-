from tkinter import *
import DefVar
import PageLogin
from PIL import ImageTk,Image
from ModulPenjual import PageJual, BerandaPenjual, ShowPenjual

def pagePenjual(frame):
    frame.destroy()
    menu = Frame(DefVar.root, bg=DefVar.background)
    menu.place(x=0, y=0, height=600, width=200)

    # berandaframe = Frame(DefVar.root, bg=DefVar.white)
    # berandaframe.place(x=200, y=0, height=600, width=600)

    DefVar.username = "Sokka"
    BerandaPenjual.BerandaPenjual()

    #Foto Profil
    img = Image.open("../Foto/pengguna/sokka.png")
    wImg, hImg = img.size
    if(wImg>hImg):
        hImg = hImg*95//wImg
        wImg = 95
    else:
        wImg = wImg*95//hImg
        hImg = 95
    img = img.resize((wImg, hImg), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(menu, image=img)
    panel.place(x=50,y=80)
    panel.img=img

    username = Label(menu, text=DefVar.username, font="Helvetica 12 bold", bg=DefVar.background, fg=DefVar.white)
    username.place(x=50, y=200, anchor=W)

    beranda = Button(menu, text="Beranda", font= DefVar.font, activebackground=DefVar.redcolor, fg=DefVar.white, bg=DefVar.background, padx=15, pady=5, relief=FLAT, width=10, command=BerandaPenjual.BerandaPenjual)
    beranda.place(x=40, y=300, anchor=W)

    jual = Button(menu, text="Jual", font= DefVar.font, activebackground=DefVar.redcolor, fg=DefVar.white, bg=DefVar.background, padx=15, pady=5, relief=FLAT, width=10, command=PageJual.jualProduk)
    jual.place(x=40, y=350, anchor=W)

    back = Button(menu, text="Back", font= "Helvetica 8", activebackground=DefVar.redcolor, fg=DefVar.white, bg=DefVar.background, relief=FLAT, command=lambda:PageLogin.start(menu))
    back.place(x=10, y=20, anchor=W)