from tkinter import *

def clickMe():
    print(i1.get()+i2.get()+i3.get())


root=Tk()

i1=IntVar()
i2=IntVar()
i3=IntVar()

checkbox1=Checkbutton(root, text="GitHub",variable=i1)
checkbox1.pack()
checkbox2=Checkbutton(root, text="RedHat",variable=i2)
checkbox2.pack()
checkbox3=Checkbutton(root, text="StackOverflow",variable=i3)
checkbox3.pack()

button=Button(root,text="Click Me",command=clickMe)
button.pack()

root.geometry("300x300+120+120")
root.mainloop()
