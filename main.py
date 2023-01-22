from tkinter import *



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50, bg="#243763")

canvas = Canvas(width=250, height=200, bg="#243763", highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=1)

website_label = Label(text="Website:", fg="White", bg="#243763", font=("Courier", 12, "bold"))
website_label.grid(row=2, column=0)
entry_website = Entry(width=49, highlightthickness=1)
entry_website.insert(END, string=" ")
entry_website.grid(row=2, column=1, sticky='w')

credentials_label = Label(text="Email/Username:", fg="White", bg="#243763", font=("Courier", 12, "bold"))
credentials_label.grid(row=3, column=0)
entry_credentials= Entry(width=49, highlightthickness=1)
entry_credentials.insert(END, string=" ")
entry_credentials.grid(row=3, column=1, sticky='w')

password_label = Label(text="Password:", fg="White", bg="#243763", font=("Courier", 12, "bold"))
password_label.grid(row=4, column=0)
entry_password = Entry(width=24, highlightthickness=1)
entry_password.insert(END, string=" ")
entry_password.grid(row=4, column=1, sticky='w')

generate_button = Button(text="Generate Password", fg="White", bg="#FF6E31", font=("Courier", 8, "bold")) #command=button_clicked
generate_button.grid(row=4, column=1, sticky="e")

add_button = Button(text="Save", fg="White", bg="#FF6E31", font=("Courier", 8, "bold")) #command=button_clicked
add_button.grid(row=5, column=1, sticky="w")
add_button.config(padx=20, pady=1)


window.mainloop()