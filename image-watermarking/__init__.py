import customtkinter
from watermarker import watermark_image


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.resizable(False, False)
root.title("Image Watermarker")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)


label = customtkinter.CTkLabel(master=frame, text="Image Watermarking App")
label.pack(pady=12, padx=10)

image_url = customtkinter.CTkEntry(master=frame, width=300, placeholder_text="Enter the image url")
image_url.pack(pady=12, padx=10)

watermark_text = customtkinter.CTkEntry(master=frame, width=300, placeholder_text="Enter the text")
watermark_text.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, width=200, text="Watermark",
                                 command=lambda: watermark_image(image_url.get(), watermark_text.get()))
button.pack(pady=12, padx=10)

root.mainloop()
