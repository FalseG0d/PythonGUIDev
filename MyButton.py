from tkinter import *


class MyButton:
    def __init__(self,master):
        self.printButton=Button(master,text="print",command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton=Button(master,text="Quit",command=master.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Hello World")
        
root=Tk()

b=MyButton(root)

root.mainloop()
