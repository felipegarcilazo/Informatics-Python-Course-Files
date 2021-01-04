#Problem 9.20 and 9.21
from tkinter import *
from tkinter.messagebox import showinfo
import random

class Application(Frame):
    # the random number that the user has to guess.
    gen_num = random.randrange(0, 10)

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
# the labels, entry, and button needed. The enter button also stimulates clicking
# the enter button.
    def create_widgets(self):
        self.lbl = Label(self, text="Enter your guess:")
        self.lbl.grid()
        self.ent = Entry(self, width = 20)
        self.ent.grid()
        self.ent.bind("<KeyPress>", self.key_press)
        self.ent.focus_set()
        self.bttn1 = Button(self, text = "Enter", command = self.guess)
        self.bttn1.grid()

    def key_press(self, event):
        if event.keysym == "Return":
            self.guess()

# Tells the user if they guessed correct and tells them if they got it
# wrong in a new window.
    def guess(self):
        if str(self.ent.get()) == str(self.gen_num):
            showinfo(message = "You have guessed the correct number " + \
                     str(self.ent.get()))
        else:
            showinfo(message = "You have guessed the wrong number")

# main
root = Tk()
root.title("tk")
root.geometry("200x100")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
