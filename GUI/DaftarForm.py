from tkinter import *
import DefVar

def daftarForm():
    frame = Frame(DefVar.root, bg=DefVar.white)
    frame.place(x=0,y=0,height=600, width=800)

    
    x_ = 200
    y_ = 100

    database = Label(frame, text="Database", font="Helvetica 10", bg=DefVar.white, fg=DefVar.text)
    database.place(x=x_+83, y=y_+85)
    vDatabase = StringVar()
    db = Entry(frame, bd=1, bg=DefVar.white, relief=GROOVE, width=40, textvariable=vDatabase)
    db.place(x=x_+83, y=y_+110)

    Password = Label(frame, text="Password", font="Helvetica 10", bg=DefVar.white, fg=DefVar.text)
    Password.place(x=x_+83, y=y_+150)
    vPassword = StringVar()
    pw = Entry(frame, bd=1, bg=DefVar.white, relief=GROOVE, width=40, textvariable=vPassword, show="*")
    pw.place(x=x_+83, y=y_+175)

    signin = Button(frame, text="Daftar", font=DefVar.font, activebackground=DefVar.background, fg=DefVar.white, bg=DefVar.redcolor, padx=15, pady=5, relief=FLAT, width=10)
    signin.place(x=x_+140, y=y_+250)

    #back
    back = Button(frame, text="Back", font= "Helvetica 8", activebackground=DefVar.redcolor, fg=DefVar.background, bg=DefVar.white, relief=FLAT, command=lambda:destroy(frame))
    back.place(x=10, y=20, anchor=W)

def destroy(frame):
    frame.destroy()