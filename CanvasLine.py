from tkinter import *

root=Tk()
canvas=Canvas(root,width=200,height=200,bg="blue")
canvas.pack()

line=canvas.create_line(0,0,200,50)
colored_line=canvas.create_line(200,50,0,100,fill="red")

root.geometry("400x400+120+120")
root.mainloop()
