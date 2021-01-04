from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        #self.state = False
        self.click = 0
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text="Click to increment!")
        self.lbl.grid()
        #self.bttn1 = Button(self, text = "South Bend, IN")
        #self.bttn1.grid()
        #self.bttn2 = Button(self, text = "California")
        #self.bttn2.grid()
        #self.bttn3 = Button(self, text = "Mexico")
        #self.bttn3.grid()
        #self.bttn4 = Button(self, text = "Chicago, IL")
        #self.bttn4.grid()
        #self.bttn5 = Button(self, text = "Light Swith: Off",
        #                   command = self.update_button)
        #self.bttn5.grid()
        self.bttn6 = Button(self, text = "Total Clicks " + str(self.click),
                            command = self.clicks)
        self.bttn6.grid()
        self.bttn7 = Button(self, text = "Reset", command = self.reset)
        self.bttn7.grid()

        
    def clicks(self):
        self.click += 1
        self.bttn6["text"] = "Total Clicks " + str(self.click)

    def reset(self):
        self.click 22= 0
        self.bttn6["text"] = "Total Clicks " + str(self.click)

    #def update_button(self):
    #    if self.state:
     #       self.bttn5["text"] = "Light Switch: On"
     #       self.state = False
     #   else:
     #       self.bttn5["text"] = "Light Switch: Off"
     #       self.state = True

root = Tk()

root.title("Basic Application Class GUI")
root.geometry("400x400")
root.resizable(width = False, height = False)

app = Application(root)

root.mainloop()
