from tkinter import *

root=Tk()
canvas=Canvas(root,width=200,height=200,bg="blue")
canvas.pack()

canvas.create_rectangle(20,20,100,100)
canvas.create_rectangle(150,20,50,100,fill="yellow",outline="red")

root.mainloop()
