from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def safe():
    website = website_input.get()
    password = password_input.get()
    email = email_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you fill all blank!")

    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            # saving new updated
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------------------    FIND PASSWORD      -----------------------------------


def find_password():
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="oops", message="You don't have any data with us!")
    else:
        for key, att in data.items():
            password = att["password"]
            if key == website_input.get():
                messagebox.showinfo(message=f"Website: {key} \n"
                                            f"password: {password}")
            else:
                website_input.delete(0, END)
                messagebox.showinfo(title="oops", message=f"No details for {website_input.get()}!")
    finally:
        website_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, row=0)

website_label = Label(text="website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(row=1, column=1)
website_input.focus()
web_input = website_input.get()

search = Button(text="search", width=12, command=find_password)
search.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, )
email_input.insert(END, "adeyemihaki@gmail.com")
email_input.get()

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=35)
password_input.grid(column=1, row=3)

Generate_button = Button(text="Generate Password", command=password_generator)
Generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=safe)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
