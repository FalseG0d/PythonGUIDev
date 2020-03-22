from tkinter import *

def printWorld():
    print("Hello World")

root=Tk()

main_menu=Menu(root)
root.config(menu=main_menu)

fileMenu=Menu(main_menu)
main_menu.add_cascade(label="file", menu=fileMenu)

editMenu=Menu(main_menu)
main_menu.add_cascade(label="edit", menu=editMenu)
editMenu.add_command(label="Print", command=printWorld)

fileMenu.add_command(label="Print", command=printWorld)

fileMenu.add_separator()

fileMenu.add_command(label="Print Same Thing", command=printWorld)

fileMenu.add_cascade(label="Menu in Menu", menu=editMenu)

root.mainloop()
