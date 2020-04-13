from tkinter import *
import DefVar
import DaftarForm
from ModulFungsi import tes
import PageLogin

DefVar.root.title("GaRas")
DefVar.root.geometry("800x600+200+50")
DefVar.root.configure(background = DefVar.white)

loginframe = Frame(DefVar.root, bg=DefVar.white)
loginframe.place(x=0,y=0,height=600, width=800)

x_ = 200
y_ = 100

database = Label(loginframe, text="Database", font="Helvetica 10", bg=DefVar.white, fg=DefVar.text)
database.place(x=x_+83, y=y_+85)
vDatabase = StringVar()
db = Entry(loginframe, bd=1, bg=DefVar.white, relief=GROOVE, width=40, textvariable=vDatabase)
db.place(x=x_+83, y=y_+110)

Password = Label(loginframe, text="Password", font="Helvetica 10", bg=DefVar.white, fg=DefVar.text)
Password.place(x=x_+83, y=y_+150)
vPassword = StringVar()
pw = Entry(loginframe, bd=1, bg=DefVar.white, relief=GROOVE, width=40, textvariable=vPassword, show="*")
pw.place(x=x_+83, y=y_+175)

signin = Button(loginframe, text="Masuk", font=DefVar.font, activebackground=DefVar.background, fg=DefVar.white, bg=DefVar.redcolor, padx=15, pady=5, relief=FLAT, width=10, command=lambda: [tes.SetDB(vPassword.get(), vDatabase.get()), PageLogin.start(loginframe)])
signin.place(x=x_+140, y=y_+250)

signup = Label(loginframe, text="Belum punya database?", font="Helvetica 8", bg=DefVar.white, fg=DefVar.text)
signup.place(x=x_+120, y=y_+292)

Daftar = Button(loginframe, text="Daftar", font="Helvetica 8", activebackground=DefVar.redcolor, activeforeground=DefVar.white, fg=DefVar.redcolor, bg=DefVar.white, relief=FLAT, command=DaftarForm.daftarForm)
Daftar.place(x=x_+240, y=y_+290)

DefVar.root.mainloop()