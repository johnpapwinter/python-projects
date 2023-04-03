import tkinter as tk


class TypoSpeedometerUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Typing Speedometer")
        self.geometry("500x350")

        self.label = tk.Label(self)
        self.label.place(x=35, y=15)

        self.countdown(60)

    def countdown(self, count):
        self.label['text'] = count

        if count > 0:
            self.after(1000, self.countdown, count-1)




