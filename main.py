import tkinter as tk
from tkinter.font import BOLD
from finestra_credenziali import sign_in, photo_converter
from classUtente import Utente
from tkinter import messagebox
import smtplib
from tkinter import END


def send():
    receiver_email = receiver_entry.get()

    check = receiver_email
    check = check[-10:]

    if check != "@gmail.com":
        messagebox.showerror(title="Errore", message="Bisogna inserire un email con dominio @gmail.com")

    else:
        try:
            s = smtplib.SMTP('smtp.gmail.com', port=587)  # create an SMTP session

            s.starttls()

            s.login(str(user.email), str(user.password))  # verify

            message = message_text.get("1.0", END)

            s.sendmail(str(user.email), receiver_email, str(message))

            s.quit()

        except:
            messagebox.showerror(title="Errore", message="Qualcosa è andato storto :(")


if __name__ == '__main__':
    user = Utente()

    temp_info = sign_in()

    user.email = temp_info[0]
    user.password = temp_info[1]

    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.geometry("900x600")
    window.configure(background="#e6e1e1")

    logo_image = photo_converter("assets/LOGO.gif", 200, 200)

    logo = tk.Label(window,
                    image=logo_image,
                    height=110,
                    background="#e6e1e1").place(x=350, y=0)

    tk.Label(window,
             text="Destinatario",
             font=("Verdana", 15, BOLD),
             background="#e6e1e1",
             foreground="#05366b").place(x=10, y=220)

    receiver_entry = tk.Entry(window,
                              font=("Arial", 15),
                              width=28,
                              background="#c3ccd6")
    receiver_entry.place(x=160, y=225)

    tk.Label(window,
             text="Corpo",
             font=("Verdana", 15, BOLD),
             background="#e6e1e1",
             foreground="#05366b").place(x=10, y=280)

    message_text = tk.Text(window,
                           width=35,
                           height=12,
                           font=("Arial", 15),
                           background="#c3ccd6")

    message_text.place(x=150, y=285)

    airplane_image = photo_converter("assets/logo1.gif", 130, 100)

    tk.Label(window, image=airplane_image, background="#e6e1e1").place(x=740, y=490)

    tk.Button(window, text="Invia",
              font=("Arial", 17, BOLD),
              foreground="#05366b",
              background="#e6e1e1",
              activebackground="#e6e1e1",
              activeforeground="#05366b",
              command=send).place(x=820, y=10)

    window.mainloop()
