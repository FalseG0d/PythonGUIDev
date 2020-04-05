from tkinter import *

def clickMe():
    s1=s.get()
    print(s1)


root=Tk()

s=StringVar()

entry=Entry(root,textvariable=s)
s.set("Welcome")

entry.pack()

button=Button(root,text="Click",command=clickMe)
button.pack()

root.geometry("300x300+120+120")
root.mainloop()
