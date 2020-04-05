from tkinter import *

def clickMe():
    print(entry.get())

root=Tk()
entry=Entry(root)
entry.pack()

button=Button(root,text="Click",command=clickMe)
button.pack()

root.geometry("300x300+120+120")
root.mainloop()
