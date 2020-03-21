from tkinter import *

root=Tk()
#To create a Window

label=Label(root,text="Hello World")
#To create text on label and connect it to root
label.pack()
#to put it on root

root.mainloop()
#To avoid closing until close button is clicked
