from tkinter import *

class Application(Frame):
    # this keeps track of where it is without h
    x, y = 20, 20

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Create variable for line width chosen and line color chosen
        self.line_width = StringVar()
        self.line_width.set(None)
        
        self.line_color = StringVar()
        self.line_color.set(None)

        # This stores the images that will be used for buttons
        self.caesar = PhotoImage(file = "roman.gif")
        self.face = PhotoImage(file = "random.gif")
        
        # All labels, entries, and buttons
        self.lbl1 = Label(self, text = "Roman Numberal Canvas").grid(row = 0, column = 2, sticky = E)
        self.lbl2 = Label(self, text = "Number:").grid(row = 1, column = 3)
        self.lbl3 = Label(self, text = "Line Width:").grid(row = 2, column = 3)
        self.lbl4 = Label(self, text = "Line Color:").grid(row = 3, column = 3)
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 4)
        self.num = BooleanVar()
        Checkbutton(self, text = "Numbers", variable = self.num).grid(row = 1, column = 5)
        Radiobutton(self, text = "1", variable = self.line_width, value = 1).grid(row = 2, column = 4)
        Radiobutton(self, text = "3", variable = self.line_width, value = 3).grid(row = 2, column = 5, sticky = W)
        Radiobutton(self, text = "5", variable = self.line_width, value = 5).grid(row = 2, column = 6, sticky = W)
        Radiobutton(self, text = "Black", variable = self.line_color, value = "Black").grid(row = 3, column = 4)
        Radiobutton(self, text = "Red", variable = self.line_color, value = "Red").grid(row = 3, column = 5, sticky = W)
        Radiobutton(self, text = "Blue", variable = self.line_color, value = "Blue").grid(row = 3, column = 6, sticky = W)
        self.button1 = Button(self, image = self.caesar, command = self.roman_num).grid(row = 4, column = 4)
        self.button1 = Button(self, image = self.face).grid(row = 4, column = 5, columnspan = 2)

# This part is in charge of creating the canvas
        self.canvas = Canvas(self, height=310, width=500)
        self.canvas.grid(row = 1, column = 0, rowspan = 5, columnspan = 3)

        self.canvas.bind("<Button-1>", self.begin)
        self.canvas.bind("<Button1-Motion>", self.draw)

        self.oldx, self.oldy = 0,0

    def begin(self, event):
        self.oldx, self.oldy = event.x, event.y

    def draw(self, event):
        newx, newy = event.x, event.y

        self.canvas.create_line(self.oldx, self.oldy, newx, newy)

        self.oldx, self.oldy = newx, newy
        
# Definition for creating roman numerals on the canvas
    def roman_num(self):
        start_x, start_y = self.x, self.y
        #THis checks for a roman number. if it does not find one it will move on
        # but if it does then it will draw it.
        if "I" not in self.pw_ent.get():
            pass
        # This is the part that actually draws the letters.
        # This elif checks for a width and puts the chosen width if there is one selected. I did not have
        # enough time to get color in one is chosen or if both were chosen but I would do a similar way if 
        elif self.line_width.get() != "None":
            for letter in self.pw_ent.get():
                if letter == "I":
                    self.canvas.create_line(start_x, start_y, start_x + 20, start_y, width = self.line_width.get())
                    self.canvas.create_line(start_x + 10, start_y, start_x + 10, start_y + 40, width = self.line_width.get())
                    self.canvas.create_line(start_x, start_y + 40, start_x + 20, start_y + 40, width = self.line_width.get())
                if letter == "D":
                    self.canvas.create_line(start_x, start_y, start_x, start_y + 40, width = self.line_width.get())
                    self.canvas.create_line(start_x, start_y, start_x + 20, start_y + 20, width = self.line_width.get())
                    self.canvas.create_line(start_x, start_y + 40, start_x + 20, start_y + 20, width = self.line_width.get())
                if letter == "C":
                    self.canvas.create_line(start_x, start_y + 10, start_x, start_y + 30, width = self.line_width.get())
                    self.canvas.create_line(start_x, start_y + 10, start_x + 10, start_y, width = self.line_width.get())
                    self.canvas.create_line(start_x + 10, start_y, start_x + 20, start_y, width = self.line_width.get())
                    self.canvas.create_line(start_x, start_y + 30, start_x + 5, start_y + 40, width = self.line_width.get())
                    self.canvas.create_line(start_x + 5, start_y + 40, start_x + 20, start_y + 40, width = self.line_width.get())
                if letter == "M":
                    self.canvas.create_line(start_x, start_y, start_x, start_y + 40, width = self.line_width.get())
                    self.canvas.create_line(start_x, start_y, start_x + 10, start_y + 10, width = self.line_width.get())
                    self.canvas.create_line(start_x + 10, start_y + 10, start_x + 20, start_y, width = self.line_width.get())
                    self.canvas.create_line(start_x + 20, start_y, start_x + 20, start_y + 40, width = self.line_width.get())
                if letter == "L":
                    self.canvas.create_line(start_x, start_y, start_x, start_y + 40, width = self.line_width.get())
                    self.canvas.create_line(start_x, start_y + 40, start_x + 20, start_y + 40, width = self.line_width.get())
                if letter == "X":
                    self.canvas.create_line(start_x, start_y, start_x + 20, start_y + 40, width = self.line_width.get())
                    self.canvas.create_line(start_x, start_y + 40, start_x + 20, start_y, width = self.line_width.get())
                if letter == "V":
                    self.canvas.create_line(start_x, start_y, start_x + 10, start_y + 40, width = self.line_width.get())
                    self.canvas.create_line(start_x + 10, start_y + 40, start_x + 20, start_y, width = self.line_width.get())
                start_x += 30
                self.x += 30
        else:
            for letter in self.pw_ent.get():
                if letter == "I":
                    self.canvas.create_line(start_x, start_y, start_x + 20, start_y)
                    self.canvas.create_line(start_x + 10, start_y, start_x + 10, start_y + 40)
                    self.canvas.create_line(start_x, start_y + 40, start_x + 20, start_y + 40)
                if letter == "D":
                    self.canvas.create_line(start_x, start_y, start_x, start_y + 40)
                    self.canvas.create_line(start_x, start_y, start_x + 20, start_y + 20)
                    self.canvas.create_line(start_x, start_y + 40, start_x + 20, start_y + 20)
                if letter == "C":
                    self.canvas.create_line(start_x, start_y + 10, start_x, start_y + 30)
                    self.canvas.create_line(start_x, start_y + 10, start_x + 10, start_y)
                    self.canvas.create_line(start_x + 10, start_y, start_x + 20, start_y)
                    self.canvas.create_line(start_x, start_y + 30, start_x + 5, start_y + 40)
                    self.canvas.create_line(start_x + 5, start_y + 40, start_x + 20, start_y + 40)
                if letter == "M":
                    self.canvas.create_line(start_x, start_y, start_x, start_y + 40)
                    self.canvas.create_line(start_x, start_y, start_x + 10, start_y + 10)
                    self.canvas.create_line(start_x + 10, start_y + 10, start_x + 20, start_y)
                    self.canvas.create_line(start_x + 20, start_y, start_x + 20, start_y + 40)
                if letter == "L":
                    self.canvas.create_line(start_x, start_y, start_x, start_y + 40)
                    self.canvas.create_line(start_x, start_y + 40, start_x + 20, start_y + 40)
                if letter == "X":
                    self.canvas.create_line(start_x, start_y, start_x + 20, start_y + 40)
                    self.canvas.create_line(start_x, start_y + 40, start_x + 20, start_y)
                if letter == "V":
                    self.canvas.create_line(start_x, start_y, start_x + 10, start_y + 40)
                    self.canvas.create_line(start_x + 10, start_y + 40, start_x + 20, start_y)
                start_x += 30
                self.x += 30
                
# main
root = Tk()
root.title("Roman Numerals")
root.geometry("900x350")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
