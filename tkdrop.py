from tkinter import *
def donothing():
    print("submenu")
root =Tk()
menu=Menu(root)
root.config(menu=menu)
subMenu=Menu(menu)#MENU
menu.add_cascade(label="File",menu=subMenu)
#submenu of file
subMenu.add_command(label="new project",command=donothing)

subMenu.add_command(label="new",command=donothing)
subMenu.add_command(label="setting",command=donothing)

subMenu.add_command(label="open",command=donothing)
subMenu.add_separator()#adding the file after open


subMenu.add_command(label="exit",command=quit)

subMenu=Menu(menu)
menu.add_cascade(label="edit",menu=subMenu)
subMenu.add_command(label="cut")
subMenu.add_command(label="copy")
subMenu.add_command(label="paste")
root.mainloop()
