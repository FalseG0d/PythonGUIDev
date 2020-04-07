from tkinter import *

def clickMe():
    print(i.get())


root=Tk()

i=IntVar()

r1=Radiobutton(root, text="GitHub",variable=i,value=1)
r1.pack()
r2=Radiobutton(root, text="RedHat",variable=i,value=2)
r2.pack()

button=Button(root,text="Click Me",command=clickMe)
button.pack()

root.geometry("300x300+120+120")
root.mainloop()
