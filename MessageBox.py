from tkinter import *
from tkinter import messagebox

def call_me():
    messagebox.showinfo("Success","Hello World")
    #messagebox.showerror("Success","Hello World")
    #messagebox.showwarning("Success","Hello World")

def ask_question():
    #answer=messagebox.yesnocancel("Exit","Are you sure?")
    answer=messagebox.askquestion("Exit","Are you sure?")
    #print(answer)
    if answer=='yes':
        root.quit()
    
root=Tk()

b1=Button(root,text="Message",command=call_me)
b1.pack()

b2=Button(root,text="Exit",command=ask_question)
b2.pack()

root.geometry("300x150+120+120")
#width x height+(distance from x axis)+(distance from y axis)
root.mainloop()
