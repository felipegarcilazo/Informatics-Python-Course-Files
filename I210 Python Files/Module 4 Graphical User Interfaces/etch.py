from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.canvas = Canvas(self, height=200, width = 300)
        self.canvas.grid(row = 0, column = 0, rowspan = 3)

        self.button_up = Button(self, text='UP', command=self.up)
        self.button_up.grid(row = 0, column = 1, columnspan = 2)

        self.button_left = Button(self, text='LEFT', command=self.left)
        self.button_left.grid(row = 1, column = 1)

        self.button_right = Button(self, text='RIGHT', command=self.right)
        self.button_right.grid(row = 1, column = 2)

        self.button_down = Button(self, text='DOWN', command=self.down)
        self.button_down.grid(row = 2, column = 1, columnspan = 2)

        self.run_text = Button(self, text = "Run Pattern", command = self.run)
        self.run_text.grid(row = 2, column = 0, sticky = E)

        self.ent = Entry(self, width = 20)
        self.ent.grid(row = 2, column = 0, sticky = W)

        #start the 'pen' in the center of the screen
        self.x, self.y = 150, 100

    def up(self):
        self.canvas.create_line(self.x, self.y, self.x, self.y - 20)
        self.y -= 20
        
    def down(self):
        self.canvas.create_line(self.x, self.y, self.x, self.y + 20)
        self.y += 20

    def left(self):
        self.canvas.create_line(self.x, self.y, self.x - 20, self.y)
        self.x -= 20
        
    def right(self):
        self.canvas.create_line(self.x, self.y, self.x + 20, self.y)
        self.x += 20

    def run(self):
        text = self.ent.get()
        for i in range(len(text)):
            if text[i] == "U":
                self.up()
            elif text[i] == "D":
                self.down()
            elif text[i] == "L":
                self.left()
            elif text[i] == "R":
                self.right()
                
# main
root = Tk()
root.title("Draw With Buttons!")
root.geometry("400x210")

app = Application(root)
root.mainloop()
