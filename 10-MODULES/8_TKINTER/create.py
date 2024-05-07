import tkinter
from tkinter.constants import LEFT, RIGHT, TOP
root = tkinter.Tk()
root.title("create")
root.geometry("235x567")
root.configure(bg="red",border=20,cursor="circle")
root.minsize(100,200)
root.maxsize(500,800)
root.mainloop()