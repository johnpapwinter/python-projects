import customtkinter as tk
import CTkMessagebox

FONT_TITLE = ("Verdana", 24)
FONT_REGULAR = ("Verdana", 18)


class TypoSpeedometerUI(tk.CTk):
    def __init__(self):
        tk.CTk.__init__(self)
        self.title("Typing Speedometer")
        self.geometry("500x450")

        self.label = tk.CTkLabel(self, text="Typing Speedometer", font=FONT_TITLE)
        self.label.pack(padx=35, pady=15)

        self.after_id = None
        self.timer = tk.CTkLabel(self, text="Timer", font=FONT_REGULAR)
        self.timer.pack(padx=35, pady=15)

        # label showing random word
        self.word = tk.CTkLabel(self, text="PLACEHOLDER", font=FONT_REGULAR)
        self.word.pack(padx=15, pady=25)

        # text area for input
        self.entry = tk.CTkEntry(self, font=FONT_REGULAR, width=300, justify="center")
        self.entry.pack(padx=15, pady=25)
        self.bind('<space>', self.handle_next_word)

        # start / stop buttons
        self.start_btn = tk.CTkButton(self, text="Start", font=FONT_REGULAR, command=self.start)
        self.start_btn.pack(padx=5, side='left', anchor='e', expand=True)

        self.stop_btn = tk.CTkButton(self, text="Stop", font=FONT_REGULAR,
                                     fg_color='red', hover_color='red', command=self.stop)
        self.stop_btn.pack(padx=5, side='right', anchor='w', expand=True)

    def countdown(self, count):
        self.timer.configure(text=f"{count}", font=FONT_REGULAR)

        if count > 0:
            self.after_id = self.after(1000, self.countdown, count-1)
        elif count == 0:
            self.after_cancel(self.after_id)
        # Logic for stopping the process goes here, probably call a func to stop everything

    def handle_next_word(self, event):
        # compare words and fetch next
        # focus on input text again
        self.word.configure(text=f"{self.entry.get()}")
        self.entry.delete(0, 'end')
        self.entry.focus()

    def start(self):
        self.countdown(60)
        print("START PRESSED")

    def stop(self):
        self.after_cancel(self.after_id)
        print("STOP PRESSED")
