from tkinter import *
class App(Frame):
    def click(self):
        if (self.E3.select_present()):
            self.S.set(self.E3.selection_get())
        
    def __init__(self, master=None,  Title = "Application", **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.title(Title)
        self.grid(sticky="NEWS")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.S = StringVar()
        self.pv = StringVar()
        self.S.set("asdadsda")
        E1 = Entry(self,  textvariable=self.S)
        E2 = Entry(self,  textvariable=self.S)
        self.E3 = Entry(self,  textvariable=self.pv)
        B = Button(self, text = "put", command = self.click)

        E1.grid(sticky = "NEWS")
        E2.grid(sticky = "NEWS")
        self.E3.grid(sticky = "NEWS")
        B.grid(sticky = "NEWS")

    

A = App()
A.mainloop()