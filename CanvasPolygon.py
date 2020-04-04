from tkinter import *

root=Tk()
canvas=Canvas(root,width=400,height=400,bg="blue")
canvas.pack()

points=[250,110,400,200,123,345,234,167]
#(x,y) all points

canvas.create_polygon(points,fill="yellow",outline="red",width=4)

root.mainloop()
