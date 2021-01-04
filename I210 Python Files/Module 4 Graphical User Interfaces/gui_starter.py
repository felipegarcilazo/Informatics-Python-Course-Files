import random
from tkinter import *

class Application(Frame):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    guesses_left = 10

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.players = StringVar()
        self.players.set(None)
        Radiobutton(self, text = "1 Player", variable = self.players,
                    value = "p1").grid()
        Radiobutton(self, text = "2 Players", variable = self.players,
                    value = "p2").grid(row = 0, column = 1)

        self.easy = BooleanVar()
        self.hard = BooleanVar()
        Checkbutton(self, text = "easy",
                    variable = self.easy).grid(row = 1, column = 0)
        Checkbutton(self, text = "hard",
                    variable = self.hard).grid(row = 1, column = 1)
        
        self.bttn1 = Button(self, text = "Let's Play", command = self.play)
        self.bttn1.grid(row = 1, column = 3)

    def opening_file(self):
        if self.easy.get() and self.hard.get():
            txt_file = open("easy_words.txt", "r")
            txt_file2 = open("hard_words.txt", "r")
            content = txt_file.readlines()
            content += txt_file2.readlines()
        elif self.easy.get():
            txt_file = open("easy_words.txt", "r")
            content = txt_file.readlines()
        elif self.hard.get():
            txt_file = open("hard_words.txt", "r")
            content = txt_file.readlines()
        for i in range(len(content)):
            content[i] = content[i].strip()
        return content

    def play(self):
        self.lbl = Label(self, text = "Guess this word").grid(row = 2,
                                                              column =0)
        self.lbl2 = Label(self, text = "-"*len(self.opening_file())).grid(row = 2,
                                                           column = 1)
        self.lbl3 = Label(self, text = "Letters left to guess:").grid(row = 3,
                                                                      column = 0)
        self.lbl4 = Label(self, text = self.alphabet).grid(row = 3, column = 1)
        self.lbl5 = Label(self, text = "Guesses Left:").grid(row = 5,
                                                             column = 0)
        self.lbl6 = Label(self, text = str(self.guesses_left)).grid(row = 5,
                                                               column = 1)
        self.ent = Entry(self, width = 30)
        self.ent.grid(row = 4, column = 1)
        self.ent.bind('<KeyPress>', self.enter_press)
        self.ent.focus_set()
    
    def enter_press(self, event):
        if event.keysym == "Return":
            letter = self.ent.get()
            self.alphabet.replace(letter, "")
            print(self.play())
            print(self.play())
            print(self.opening_file())
            if letter in self.opening_file():
                self.lbl2 = Label(self, text = "-"*len(word)).grid(row = 2,
                                                           column = 1)
        
        
        
# main
root = Tk()
root.title("Basic Application Class GUI")
root.geometry("400x200")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
