import customtkinter
from tkinter import messagebox
import tkinter
import qrcode
from time import sleep
from PIL import Image
import os

color_1 = "#57e3df"
app = customtkinter.CTk()
# System Settings

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
#App frame
app.geometry("720x520")
app.title("Qr Code generator")

# logica


def generate_qrs():
    qr_url = input_url.get()
    name = input_name_file.get()
    if qr_url == "" or name == "":
        messagebox.showwarning(title="Error",message="All inputs must be filled in")
    else:
        qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
        qr.add_data(qr_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"{os.path.join(os.path.expanduser('~'), 'Downloads')}/{name}.jpg")
        show_image = customtkinter.CTkImage(light_image=Image.open(f"{os.path.join(os.path.expanduser('~'), 'Downloads')}/{name}.jpg"),size=(200,200))
        image_label = customtkinter.CTkLabel(app,image=show_image,text="")
        image_label.grid(column=1,row=4,padx=15,pady=15)

#variables
url = tkinter.StringVar()

name_file = tkinter.StringVar()

# elements
Title = customtkinter.CTkLabel(app,text="Qr Generator",font=("Comic Mono",30))
Label_url = customtkinter.CTkLabel(app,text="Url",font=("Roboto",12,"bold"),anchor="sw",width=140,height=10,text_color=color_1)
Label_name = customtkinter.CTkLabel(app,text="Name File",font=("Roboto",12,"bold"),anchor="sw",width=140,height=10,text_color=color_1)
label_file = customtkinter.CTkLabel(app,text="Qrs are on downloads folder",font=("Roboto",11,"bold"),text_color="gray75")

input_url = customtkinter.CTkEntry(app,placeholder_text="www.youtube.com", placeholder_text_color="#fff",textvariable=url,border_width=1)
input_name_file = customtkinter.CTkEntry(app,placeholder_text="file.jpg", placeholder_text_color="#fff",textvariable=name_file,border_width=1,border_color="")



btn = customtkinter.CTkButton(app,text="Generate",command=generate_qrs)

# reorganize elements in screen
Label_url.grid(column=0,row=1)
Label_name.grid(column=1,row=1)
label_file.grid(column=1,row=0,padx=5,pady=5)
input_url.grid(column=0,row=2,padx=10)
input_name_file.grid(column=1,row=2,padx=10)
Title.grid(column=0,row=0,padx=10,pady=10)
btn.grid(column=2,row=2,padx=10)



# Run app
app.mainloop()

