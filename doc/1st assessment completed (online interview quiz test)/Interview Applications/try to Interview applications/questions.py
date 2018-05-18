from Tkinter import *

class PythonQuestions:

    Total_scores = 10
    Correct_answer = 0
    Wrong_answer = 0
    Skip_question = 0

    def selection():
        score=0
        selection = "You selected the option " + str(var.get())
        label.config(text = selection)

root = Tk()
var = IntVar()
Radiobutton(root, text="Development environment a", variable=var, value=1, command=selection).pack(anchor=W)
Radiobutton(root, text="Programming language b", variable=var, value=2, command=selection).pack(anchor=W)
Radiobutton(root, text="Set of editing tools c", variable=var, value=3, command=selection).pack(anchor=W)
label = Label(root)
label.pack()
root.mainloop()

