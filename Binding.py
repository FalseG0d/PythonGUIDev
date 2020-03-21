from tkinter import *

root=Tk()

def Call(event):
    print("I have been called")

button=Button(root, text="Click to Call", )
button.bind("<Button-1>",Call)
#To bind the event of clicking the button with any method

button.pack()

root.mainloop()
