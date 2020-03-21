from tkinter import *

root=Tk()
one=Label(root, text="One", bg="red")
two=Label(root, text="Two", bg="blue")
three=Label(root, text="Three", bg="yellow")

one.pack()
two.pack(fill=X)
#To fit the widegt accross X axis
three.pack(side=LEFT, fill=Y)
#Sie must be = LEFT to work
#To fit the widegt accross Y axis

root.mainloop()
