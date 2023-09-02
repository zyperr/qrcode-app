# import qrcode
import customtkinter


app = customtkinter.CTk()

# System Settings

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#App frame
app.geometry("720x520")
app.title("Qr Code generator")

title = customtkinter.CTkLabel(app,text="Hello")
title.pack(padx=10,pady=10)
# Run app
app.mainloop()