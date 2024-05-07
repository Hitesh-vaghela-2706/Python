from tkinter import *
import tkinter
from PIL import Image,ImageTk

root = tkinter.Tk()
root.geometry("500x500")

image = Image.open("E:\PYTHON/PROJECTS\_1_IMAGE2SKETCH_DRAW\lion.jpg")
pht = ImageTk.PhotoImage(image)

lbl = Label(image=pht)
lbl.pack()

root.mainloop()