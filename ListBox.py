from tkinter import *

root=Tk()

l=Listbox(root,width="30",height="50")

l.insert(1,"C++")
l.insert(2,"C#")
l.insert(3,"Java")
l.insert(4,"Python")

l.pack()

root.geometry("300x300+120+120")
root.mainloop()
