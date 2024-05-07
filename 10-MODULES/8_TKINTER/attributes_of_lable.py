from tkinter import *
import tkinter

root = tkinter.Tk()
root.title("attributes of lable")
root.geometry("400x400")
# we ues greed to pack a lable bacuse of using lable we can easily formate it 
# according to row and column and our data is looking too good
lbl1 = Label(text="hello this is hitesh vaghela",bg="green",fg="white",
    background="yellow",border=3,borderwidth=5,height=15,width=20,font="comicsanms 15 bold",
    foreground="blue",relief=SUNKEN)
lbl1.grid(row=1,column=1)


root.mainloop()