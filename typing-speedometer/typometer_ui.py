import customtkinter as tk
import CTkMessagebox
from typometer_service import TypoSpeedometerService

FONT_TITLE = ("Verdana", 24)
FONT_REGULAR = ("Verdana", 18)
FONT_SMALL = ("Verdana", 12)


class TypoSpeedometerUI(tk.CTk):
    def __init__(self):
        self.service = TypoSpeedometerService()
        self.word_requested = None

        tk.CTk.__init__(self)
        self.title("Typing Speedometer")
        self.geometry("500x450")
        self.resizable(False, False)

        self.label = tk.CTkLabel(self, text="Typing Speedometer", font=FONT_TITLE)
        self.label.pack(padx=35, pady=15)

        self.after_id = None
        self.timer = tk.CTkLabel(self, text="00", font=FONT_REGULAR)
        self.timer.pack(padx=35, pady=15)

        # label showing random word
        self.word = tk.CTkLabel(self, text="", font=FONT_REGULAR)
        self.word.pack(padx=15, pady=25)

        # text area for input
        self.entry = tk.CTkEntry(self, font=FONT_REGULAR, width=300, justify="center")
        self.entry.pack(padx=15, pady=25)
        self.bind('<space>', self.handle_next_word)

        self.instructions = tk.CTkLabel(self, text="Press the Spacebar to submit a word", font=FONT_SMALL)
        self.instructions.pack(padx=15, pady=5)

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
            wpm = self.service.calculate_wpm()
            self.service.reset()
            CTkMessagebox.CTkMessagebox(title="Time's up!", message=f"Congrats! Your wpm is {wpm}", icon='warning')

    def handle_next_word(self, event):
        self.service.compare_words(self.word_requested, self.entry.get())

        self.word_requested = self.service.fetch_random_word()
        self.word.configure(text=f"{self.word_requested}")

        self.entry.delete(0, 'end')
        self.entry.focus()

    def start(self):
        self.word_requested = self.service.fetch_random_word()
        self.word.configure(text=f"{self.word_requested}")
        self.countdown(60)

    def stop(self):
        self.after_cancel(self.after_id)
        self.service.reset()
