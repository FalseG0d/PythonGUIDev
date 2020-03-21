#Frames are containers invisible to user.

from tkinter import *

root=Tk()

frame=Frame(root)

btn1=Button(frame,text="Submit")
btn1.pack(side=LEFT)
btn2=Button(frame,text="Clear")
btn2.pack(side=LEFT)

frame.pack()

frameBottom=Frame(root)

btn3=Button(frameBottom,text="Cancel")
btn3.pack()

frameBottom.pack(side=BOTTOM)

root.mainloop()
