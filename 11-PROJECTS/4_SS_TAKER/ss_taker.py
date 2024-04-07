import random
x = random.randint(1,5678)
import pyautogui
# create a function to take ss
def myss():
    A = pyautogui.screenshot()
    A.save(f'E:\PYTHON\PROJECTS\4_SS_TAKER\screenshot{x}.png')
import tkinter as t
# creating a screen for take ss
root = t.Tk()
root.title("ss_taker")
# make screen canvas to change size
can1 = t.Canvas(root,height=300,width=300)
can1.pack()
# create a button to click and take ss
butn = t.Button(text='take screenshot',command=myss,bg='green',font=15,fg='white')
# show button
can1.create_window(150,150,window=butn)

root.mainloop()