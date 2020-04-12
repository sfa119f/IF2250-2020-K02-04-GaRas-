from tkinter import *
import DefVar
from ModulPembeli import showProduct

def berandaPembeli():
    berandaframe = Frame(DefVar.root, bg=DefVar.white)
    berandaframe.place(x=200, y=50, height=550, width=600)

    showProduct.showProduct(1,"Search","All")
    #Contoh Data
    #List = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]

    
