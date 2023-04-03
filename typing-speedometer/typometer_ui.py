import customtkinter as tk


class TypoSpeedometerUI(tk.CTk):
    def __init__(self):
        tk.CTk.__init__(self)
        self.title("Typing Speedometer")
        self.geometry("500x350")

        self.label = tk.CTkLabel(self)
        self.label.place(x=35, y=15)

        self.countdown(60)

    def countdown(self, count):
        self.label.configure(text=count)

        if count > 0:
            self.after(1000, self.countdown, count-1)




