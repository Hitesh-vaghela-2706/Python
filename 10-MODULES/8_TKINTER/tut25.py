from tkinter import *


class GUI(Tk):
    def _init_(self):
        super()._init_()
        self.geometry("744x377")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)

    def click(self):
        print("Button clicked")

    def createbutton(self, inptext):
        Button(text=inptext, command=self.click).pack()


if __name__ == '_main_':
    window = GUI()
    window.status()
    window.createbutton("Click me")
    window.mainloop()