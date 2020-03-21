from tkinter import *

root=Tk()

def rightClick(event):
    print("Right Click")

def leftClick(event):
    print("Left Click")
    
def middleClick(event):
    print("Middle Click")

frame=Frame(root,width=200,height=200)

frame.bind("<Button-1>", leftClick)

frame.bind("<Button-3>", rightClick)

frame.bind("<Button-2>", middleClick)

frame.pack()

root.mainloop()
