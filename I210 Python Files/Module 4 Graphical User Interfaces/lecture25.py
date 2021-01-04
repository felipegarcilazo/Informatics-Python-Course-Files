from tkinter import *
class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text="Enter student information")
        self.lbl.grid(row = 0, column = 1, columnspan = 3)
        self.lbl2 = Label(self, text = "Student name:")
        self.lbl2.grid(row = 1, column = 0, sticky = W)
        self.ent = Entry(self, width = 52)
        self.ent.grid(row = 1, column = 1, columnspan = 2, sticky = E)
        self.lbl3 = Label(self, text = "GPA:")
        self.lbl3.grid(row = 2, column = 0, sticky = W)
        self.ent2 = Entry(self, width = 52)
        self.ent2.grid(row = 2, column = 1, columnspan = 2, sticky = W)
        self.lbl4 = Label(self, text = "Essay:")
        self.lbl4.grid(row = 3, column = 0, sticky = W)
        self.txt = Text(self, width = 52)
        self.txt.grid(row = 4, column = 1, columnspan = 3, rowspan = 4)
        self.bttn1 = Button(self, text = "Save")
        self.bttn1.grid(row = 8, column = 0, sticky = E)
        self.bttn2 = Button(self, text = "Clear")
        self.bttn2.grid(row = 8, column = 2, sticky = W)


            

# main
root = Tk()
root.title("College Application")
root.geometry("550x550")
root.resizable(width = FALSE, height = FALSE)
app = Application(root)
root.mainloop()





##from tkinter import *
##class Application(Frame):
##    def __init__(self, master):
##        Frame.__init__(self, master)
##        self.grid()
##        self.create_widgets()
##
##    def create_widgets(self):
##        self.lbl = Label(self, text="Enter two numbers")
##        self.lbl.grid()
##        self.ent = Entry(self, width = 30)
##        self.ent.grid()
##        self.ent2 = Entry(self, width = 30)
##        self.ent2.grid()
##        self.lbl2 = Label(self, text = "The sum")
##        self.lbl2.grid()
##        self.bttn1 = Button(self, text = "Add the numbers", command = self.act)
##        self.bttn1.grid()
##
##    def act(self):
##        try:
##            sum1 = int(self.ent.get()) + int(self.ent2.get())
##            self.lbl2["text"] = "The sum " + str(sum1)
##        except:
##            self.lbl2["text"] = "Error: invalid value"
##        self.ent.delete(0, END)
##        self.ent2.delete(0, END)
##            
##
### main
##root = Tk()
##root.title("Basic Application Class GUI")
##root.geometry("400x200")
##root.resizable(width = FALSE, height = FALSE)
##app = Application(root)
##root.mainloop()
