from tkinter import *
import DefVar
from ModulPenjual import ShowPenjual

def BerandaPenjual():
    berandaframe = Frame(DefVar.root, bg=DefVar.white)
    berandaframe.place(x=200, y=0, height=600, width=600)

    ShowPenjual.ShowPenjual(1)
