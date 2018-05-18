class BatchIndiv():
    def __init__(self, master):
        self.master=master
        self.startwindow()
        self.b=0

    def startwindow(self):

        self.var1 = IntVar()
        self.textvar = StringVar()

        self.Label1=Label(self.master, text="Batch or indivdual import?")
        self.Label1.grid(row=0, column=0)

        self.Label2=Label(self.master, textvariable=self.textvar)
        self.Label2.grid(row=2, column=0)

        self.rb1 = Radiobutton(self.master, text="Batch", variable=self.var1,
                               value=1, command=self.cb1select)
        self.rb1.grid(row=1, column=0, sticky=W)

        self.rb2 = Radiobutton(self.master, text="Individual", variable=self.var1,
                               value=2, command=self.cb1select)
        self.rb2.grid(row=1, column=1, sticky=W)

        self.Button1=Button(self.master, text="ok", command=self.ButtonClick)
        self.Button1.grid(row=1, column=2)

    def ButtonClick(self):
         if (self.var1.get())==1:
            b=BatchImport()
            return b
            self.master.quit()
            self.master.destroy()
         elif (self.var1.get())==2:
            b=IndivImport()
            return b
            self.master.quit()
            self.master.destroy()
         else: pass

    def cb1select(self):
        return self.var1.get()

    #End of class definition.
    #Code:

    root=Tk()
    window=BatchIndiv(root)
    b=BatchIndiv.ButtonClick.b
    root.mainloop()

    '''Treat the BatchImport and IndivImport functions as black boxes, they just return an integer value, which I assign to the variable b inside ButtonClick(). I need that value to do some stuff below root.mainloop(), (i.e. where .... is), but I don't know how to get it. Tkinter is really quite irritating, especially as everyone has different methods of doing things so the online documentation is never the same - tried doing what was written in various ones and it just gave me more lovely error messages.

    Any and all help would be appreciated.

    PS - how can I make the window close when the button is pressed, and still send the value b back to the rest of the code, and not just quit python completely? As you can see I tried using .quit() and .destroy() but to no luck.
    python tkinter
    shareimprove this question
            
    asked Jul 1 '11 at 11:27
    Dave Lewis
    74311
            
    add a comment
    2 Answers
    active
    oldest
    votes
    up vote
    1
    down vote
    accepted
            

    Your variable b is just local to your class, so it the moment your class is deleted (after you do destroy or quit), b gets destroyed. So define the variable b as global.'''
    

    b = 0                    # this is now in the global namespace

class BatchIndiv():
    def __init__(self, master):
        self.master=master
        self.startwindow()
        #self.b=0      # no need for this, directly store in the global variable

    def startwindow(self):

        self.var1 = IntVar()
        self.textvar = StringVar()

        self.Label1=Label(self.master, text="Batch or indivdual import?")
        self.Label1.grid(row=0, column=0)

        self.Label2=Label(self.master, textvariable=self.textvar)
        self.Label2.grid(row=2, column=0)

        self.rb1 = Radiobutton(self.master, text="Batch", variable=self.var1,
                               value=1, command=self.cb1select)
        self.rb1.grid(row=1, column=0, sticky=W)

        self.rb2 = Radiobutton(self.master, text="Individual", variable=self.var1,
                               value=2, command=self.cb1select)
        self.rb2.grid(row=1, column=1, sticky=W)

        self.Button1=Button(self.master, text="ok", command=self.ButtonClick)
        self.Button1.grid(row=1, column=2)

    def ButtonClick(self):
        global b
        if (self.var1.get())==1:
            b=BatchImport()
            self.master.quit()
            #self.master.destroy()    # either quit or destroy, I think one is sufficient, but confirm to be sure.
        elif (self.var1.get())==2:
            b=IndivImport()
            self.master.quit()
            #self.master.destroy()    # either quit or destroy, I think one is sufficient, but confirm to be sure
        else:
             pass

    def cb1select(self):
        return self.var1.get()

#End of class definition.
#Code:

root=Tk()
window=BatchIndiv(root)
root.mainloop()

# now do here whatever you want to do with the variable b
print b
