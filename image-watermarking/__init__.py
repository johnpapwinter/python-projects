import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Image Watermarker")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)


label = customtkinter.CTkLabel(master=frame, text="Image Watermarking App")
label.pack(pady=12, padx=10)

root.mainloop()
