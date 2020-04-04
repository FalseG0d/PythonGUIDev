from tkinter import *

root=Tk()
canvas=Canvas(root,width=400,height=400,bg="blue")
canvas.pack()

canvas.create_oval(100,100,350,250,fill="yellow",outline="yellow")
canvas.create_oval(100,100,300,300)
#Refers a rectangle touching each edge

root.mainloop()
