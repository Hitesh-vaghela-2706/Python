from tkinter import *
import tkinter

root = tkinter.Tk()
root.title("frames")
root.geometry("400x400")

frm = Frame(root,bg="yellow",borderwidth=4,relief=SUNKEN)
frm.pack(fill="y",padx=10,side=LEFT)

lbl = Label(frm,text='',bg="red",fg="white",width=500)
lbl.pack(fill=Y,padx=3,side=LEFT)

root.mainloop()