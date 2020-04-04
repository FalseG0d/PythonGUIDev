from tkinter import *

root=Tk()
canvas=Canvas(root,width=200,height=200,bg="blue")
canvas.pack()

photo=PhotoImage(file="D:\\Sword.png")

canvas.create_image(20,20,image=photo, anchor=CENTER)
#coordinate, imagefile, anchor or part which starts to draw first
#Example of ANchor NW,N,NE,E,CENTER,E,SW,S,SE

root.mainloop()
