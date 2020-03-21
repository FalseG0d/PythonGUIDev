from tkinter import *

root=Tk()

name=Label(root, text="Name")

password=Label(root, text="Password")

entry1=Entry(root)
entry2=Entry(root)

name.grid(row=0,sticky=W)
# column by default 0
#sticky=W to ensure name is sticking towards Left side
#N for up S for bottom E for Left W for right
entry1.grid(row=0,column=1)

password.grid(row=1,column=0)
entry2.grid(row=1,column=1)

c=Checkbutton(root, text="Remember Me")
c.grid(columnspan=2)
#Between 2 columns

root.mainloop()
