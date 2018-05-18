from Tkinter import *
def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text = selection)

root = Tk()
var = IntVar()
Radiobutton(root, text="Option a", variable=var, value=1, command=sel).pack(anchor=W)
Radiobutton(root, text="Option b", variable=var, value=2, command=sel).pack(anchor=W)
Radiobutton(root, text="Option c", variable=var, value=3, command=sel).pack(anchor=W)
label = Label(root)
label.pack()
root.mainloop()
