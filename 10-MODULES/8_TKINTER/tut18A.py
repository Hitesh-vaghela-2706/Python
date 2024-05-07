# to create a non dropdown menu
from tkinter import *

from tut18 import myfunc
root = Tk()
# or
# import tkinter
# root = tkinter.Tk()

def myfunc():
    print("chala ja bsdk")

root.title("vs code")
root.configure(bg="#fff000")
root.geometry("600x600")

mainmenu = Menu(root)
mainmenu.add_command(label="File",command=myfunc)
mainmenu.add_command(label="Edit",command=myfunc)
mainmenu.add_command(label="View",command=myfunc)
mainmenu.add_command(label="Selection",command=myfunc)
mainmenu.add_command(label="Go",command=myfunc)
mainmenu.add_command(label="Run",command=myfunc)
mainmenu.add_command(label="Terminal",command=myfunc)
root.config(menu=mainmenu)

root.mainloop()