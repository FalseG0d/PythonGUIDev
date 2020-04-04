from tkinter import *

root=Tk()
canvas=Canvas(root,width=200,height=200,bg="blue")
canvas.pack()

canvas.create_arc(100,100,50,50)
#Point One and Point two

canvas.create_arc(150,150,50,50,extent=120)
#Point One and Point two

root.geometry("400x400+120+120")
root.mainloop()
