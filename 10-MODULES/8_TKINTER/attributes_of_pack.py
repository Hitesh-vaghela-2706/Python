from tkinter import *
import tkinter

root = tkinter.Tk()
root.title(" attributes of pack ")
root.geometry("400x400")
#  we never grid root becuse we don't need to do this 
#  if we pack or grid a root it is not wrong 
#  by default root is automaticaly packs it self
A = Label(text='I AM HITESH',bg="black",fg="white")
#  sides :- TOP,BOTTOM,LEFT,RIGHT
A.pack( anchor="se",side=TOP,pady=100,padx=15,fill=X)

root.mainloop()