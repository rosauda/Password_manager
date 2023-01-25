from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- CONSTANTS ------------------------------- #

EMAIL = "example@hotmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def create_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def saving_credentials():
    website_info = entry_website.get()
    user_name_email = entry_credentials.get()
    user_password = entry_password.get()
    new_data = {
        website_info: {
            "email": user_name_email,
            "password": user_password,
        }
    }

    if len(website_info) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # Reset entries
            entry_website.delete(0, END)
            entry_password.delete(0, END)
            if user_name_email == EMAIL:
                pass
            else:
                entry_credentials.delete(0, END)
                entry_credentials.insert(0, string=EMAIL)


# ---------------------------- UI SETUP ------------------------------- #

# Generating window
window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=350)
window.config(padx=50, pady=50, bg="#243763")

# Creating Canvas
canvas = Canvas(width=250, height=200, bg="#243763", highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=1)

# Labels
website_label = Label(text="Website:", fg="White", bg="#243763", font=("Courier", 12, "bold"))
website_label.grid(row=2, column=0)
credentials_label = Label(text="Email/Username:", fg="White", bg="#243763", font=("Courier", 12, "bold"))
credentials_label.grid(row=3, column=0)
password_label = Label(text="Password:", fg="White", bg="#243763", font=("Courier", 12, "bold"))
password_label.grid(row=4, column=0)

# Entries
entry_website = Entry(width=49, highlightthickness=1)
entry_website.grid(row=2, column=1, sticky='w')
entry_website.focus()

entry_credentials = Entry(width=49, highlightthickness=1)
entry_credentials.grid(row=3, column=1, sticky='w')
entry_credentials.insert(0, string=EMAIL)

entry_password = Entry(width=27, highlightthickness=1)
entry_password.grid(row=4, column=1, sticky='w')

# Buttons
generate_button = Button(text="Generate Password", fg="White", bg="#FF6E31",
                         font=("Courier", 8, "bold"), command=create_password)
generate_button.grid(row=4, column=1, sticky="e")

add_button = Button(text="Save", fg="White", bg="#FF6E31", font=("Courier", 8, "bold"), command=saving_credentials)
add_button.grid(row=5, column=1, sticky="w")
add_button.config(padx=20, pady=1)

window.mainloop()
