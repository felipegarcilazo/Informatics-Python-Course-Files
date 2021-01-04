from tkinter import *

class Application(Frame):
    list_1 = []

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text="Click to increment!")
        self.lbl.grid()
        self.bttn = Button(self, text = "Total Clicks: 0",
                           command = self.update_count)
        self.bttn.grid()
        self.bttn.bind('<KeyPress>', self.space_click)
        self.bttn.focus_set()

        #self.pattern = ["Up", "Up", "Down", "Down", "Left", "Right", "Left"]

    def update_count(self):
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)

    def space_click(self, event):
        if event.keysym == "Space":
            self.update_count()
        elif event.keysym == "2":
            self.bttn_clicks += self.bttn_clicks
            self.update_count()
        elif event.keysym =="BackSpace":
            self.bttn_clicks = -1
            self.update_count()

# main
root = Tk()
root.title("Click Counter 3")
root.geometry("250x75")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
