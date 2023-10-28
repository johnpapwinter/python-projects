import customtkinter as tk
import os

FONT_TITLE = ("Verdana", 24)
FONT_REGULAR = ("Verdana", 18)


class DangerousWriting(tk.CTk):
    def __init__(self):
        self.countdown = None
        tk.set_appearance_mode('dark')
        tk.set_default_color_theme('dark-blue')
        tk.CTk.__init__(self)
        self.ui()

    def count_down(self, count):
        self.textbox.configure(state=tk.NORMAL)
        if count > 0:
            self.label.configure(text=f"You have {count} seconds left!")
            self.countdown = self.after(1000, self.count_down, count - 1)
        else:
            self.textbox.delete('1.0', 'end-1c')

    def save_text(self, event: None):
        text = self.textbox.get("1.0", "end-1c")
        filename = 'dangerous_writing.txt'
        if os.path.exists(filename):
            with open(filename, 'a') as file:
                file.write(f"{text}\n")
        else:
            with open(filename, 'w') as file:
                file.write(f"{text}\n")
        self.textbox.delete('1.0', 'end-1c')
        self.textbox.insert('1.0', '')

    def start(self, event):
        self.after_cancel(self.countdown)
        self.count_down(10)

    def ui(self):
        self.geometry('600x700')
        self.resizable(False, False)
        self.title('Dangerous Writing')
        self.bind('<Control-s>', self.save_text)

        self.frame = tk.CTkFrame(self)
        self.frame.pack(padx=20, pady=20, fill='both', expand=True)

        self.label = tk.CTkLabel(self.frame, text='Press start and begin writing!', font=FONT_TITLE)
        self.label.pack(padx=10, pady=12)

        self.textbox = tk.CTkTextbox(self.frame, width=450, height=450, font=FONT_REGULAR,
                                  wrap='word', state=tk.DISABLED)
        self.textbox.pack(padx=10, pady=20)
        self.textbox.bind('<Key>', command=self.start)

        self.start_button = tk.CTkButton(self.frame, text='Start', font=FONT_REGULAR,
                                         command=lambda: self.count_down(10))
        self.start_button.pack(padx=5, side=tk.LEFT, anchor='e', expand=True)
        self.save_button = tk.CTkButton(self.frame, text='Save', font=FONT_REGULAR,
                                        fg_color='green', hover_color='green', command=self.save_text)
        self.save_button.pack(padx=5, side=tk.RIGHT, anchor='w', expand=True)

