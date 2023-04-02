from tkinter import *


def countdown(count):
    label['text'] = count

    if count > 0:
        root.after(1000, countdown, count-1)


root = Tk()
root.title("Typing Speedometer")
root.geometry("500x350")

label = Label(root)
label.place(x=35, y=15)

countdown(60)

root.mainloop()

