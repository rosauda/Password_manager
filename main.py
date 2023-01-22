from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

EMAIL = "example@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #


def saving_credentials():
    with open("data.txt", "a") as data_password:
        new_entry = f"{entry_website.get()} | {entry_credentials.get()} | {entry_password.get()} "
        data_password.write(new_entry + '\n')

        # Reset entries
        entry_website.delete(0, END)
        entry_password.delete(0, END)
        if entry_credentials.get() == EMAIL:
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
                         font=("Courier", 8, "bold"))  # command=button_clicked
generate_button.grid(row=4, column=1, sticky="e")

add_button = Button(text="Save", fg="White", bg="#FF6E31", font=("Courier", 8, "bold"), command=saving_credentials)
add_button.grid(row=5, column=1, sticky="w")
add_button.config(padx=20, pady=1)

window.mainloop()
