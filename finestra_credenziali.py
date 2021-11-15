import tkinter as tk
from PIL import Image, ImageTk
from tkinter.font import BOLD
import os
from tkinter import messagebox
from classUtente import Utente
from tkinter import END

user_registration = Utente()
temp_user = []


def photo_converter(path, size1, size2):
    image1 = Image.open(path)

    image2 = image1.resize((size1, size2), Image.ANTIALIAS)

    definitive = ImageTk.PhotoImage(image2)

    return definitive


def registration():
    file_name = entry_email.get()
    email = entry_email.get()

    password10 = entry_password.get()
    password20 = confirm_pass_entry.get()

    path = entry_path.get()

    user_registration.checkemail(email=email)

    user_registration.checkpassword(password1=password10, password2=password20)

    if not os.path.exists(path):  # if the path doesn't exist
        messagebox.showerror(title="Errore", message="Il path per il salvataggio dei dati è inesistente")

    else:  # create the data
        path += "\\"
        path += file_name
        path += ".txt"

        if os.path.isfile(path):
            messagebox.showerror(title="Errore",
                                 message="Esiste già un account registrato in questo path di salvataggio :(")

        with open(path, "w") as file:
            file.write(str(user_registration.email))
            file.write("\n" + str(user_registration.password))

        entry_email.delete(0, END)
        entry_password.delete(0, END)
        confirm_pass_entry.delete(0, END)


def login():
    user_email = entry_email.get()
    user_password = entry_password.get()

    path = entry_path.get()
    path += "\\"
    path += user_email
    path += ".txt"

    try:
        with open(path, "r") as file:
            temp_list = file.readlines()

            email = temp_list[0]
            password = temp_list[1]

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="L'account non esiste")

    if user_email in email:
        if user_password in password:
            temp_user.append(email)
            temp_user.append(password)
            window_register.destroy()
        else:
            messagebox.showerror(title="Errore", message="Email o password errati!")
    else:
        messagebox.showerror(title="Errore", message="Email o password errati!")


window_register = tk.Tk()

entry_path = tk.Entry(window_register, font=("Arial", 15), width=26, background="#c3ccd6")
entry_path.place(x=145, y=143)

entry_email = tk.Entry(window_register, font=("Arial", 15), width=28, background="#c3ccd6")
entry_email.place(x=110, y=184)

entry_password = tk.Entry(window_register, font=("Arial", 15), width=25, background="#c3ccd6", show="*")
entry_password.place(x=155, y=235)

confirm_pass_entry = tk.Entry(window_register, font=("Arial", 15), width=25, background="#c3ccd6", show="*")
confirm_pass_entry.place(x=260, y=286)


def sign_in():
    window_register.resizable(width=False, height=False)
    window_register.geometry("600x400")
    window_register.configure(background="#e6e1e1")

    image_registration = photo_converter("assets/REGISTER_NOW.gif", 200, 200)

    tk.Label(window_register,
             image=image_registration,
             height=109,
             background="#e6e1e1").place(x=220, y=0)

    tk.Label(window_register,
             text="Percorso",
             font=("Verdana", 15, BOLD),
             background="#e6e1e1",
             foreground="#05366b").place(x=24, y=140)

    tk.Label(window_register,
             text="Email",
             font=("Verdana", 15, BOLD),
             background="#e6e1e1",
             foreground="#05366b").place(x=24, y=180)

    tk.Label(window_register,
             text="Password",
             font=("Verdana", 15, BOLD),
             background="#e6e1e1",
             foreground="#05366b").place(x=24, y=230)

    tk.Label(window_register,
             text="Conferma Password",
             font=("Verdana", 15, BOLD),
             background="#e6e1e1",
             foreground="#05366b").place(x=24, y=280)

    tk.Button(text="Registrati",
              font=("Verdana", 15, BOLD),
              background="#e6e1e1",
              foreground="#05366b",
              activebackground="#e6e1e1",
              activeforeground="#05366b",
              command=registration).place(x=5, y=350)

    tk.Button(text="Login",
              font=("Verdana", 15, BOLD),
              background="#e6e1e1",
              foreground="#05366b",
              activebackground="#e6e1e1",
              activeforeground="#05366b",
              command=login).place(x=510, y=350)

    window_register.mainloop()

    return temp_user
