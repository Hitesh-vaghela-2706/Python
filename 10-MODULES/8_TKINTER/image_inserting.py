# this code works only for png files...
from tkinter import *
import tkinter

root = tkinter.Tk()
root.geometry("300x200") 

photo = PhotoImage(file="E:\PYTHON\PROJECTS\_1_IMAGE2SKETCH_DRAW\lion.png")

lbl = tkinter.Label(image=photo)
lbl.pack()
root.mainloop()