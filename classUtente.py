from tkinter import messagebox


class Utente:
    def __init__(self):
        self._email = None
        self._password = None

    def checkemail(self, email):
        check = email

        check = check[-10:]  # salvo in check solo la parte @gmail.com

        if check != "@gmail.com":  # se non corrisponde lancio un errore
            messagebox.showerror(title="Errore", message="Bisogna inserire un email con dominio @gmail.com")
            return False

        else:
            self._email = email
            return True

    def checkpassword(self, password1, password2):
        if password1 != password2:  # se le password sono diverse
            messagebox.showerror(title="Errore", message="Le password non corrispondono :(")

        elif len(password1) < 6:  # se la password è minore di 6
            messagebox.showerror(title="Errore", message="La password deve essere lunga almeno 6 caratteri :(")

        else:
            self._password = password1

    def get_email(self):
        return self._email

    def get_pass(self):
        return self._password

    def set_email(self, email):
        self._email = email

    def set_pass(self, password):
        self._password = password

    email = property(get_email, set_email)
    password = property(get_pass, set_pass)