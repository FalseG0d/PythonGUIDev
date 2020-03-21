#Frames are containers invisible to user.

from tkinter import *

root=Tk()
frame=Frame(root)
btn1=Button(frame,text="Submit")
btn1.pack()
btn2=Button(frame,text="Clear")
btn2.pack()
btn3=Button(frame,text="Cancel")
btn3.pack()

frame.pack()

root.mainloop()
