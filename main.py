from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols= [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers= [choice(numbers) for _ in range(randint(2, 4))]


    password_list= password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password= "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_data(website, email, password):

    is_ok=messagebox.askokcancel(title=f"Confirmation for: {website}", message=f"These are the details you entered: \nEmail:{email}"
                                                  f"\nPassword: {password} \nIts ok to save?")

    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"Website: {website} | Email/User: {email} | Password: {password}\n")

def add_button_click():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="ERROR", message="Please don't leave any fields empty!")
    else:
        save_to_data(website, email, password)
        website_entry.delete(0, END)
        email_user_entry.delete(0, END)
        password_entry.delete(0, END)

def show_data():
    try:
        os.system("notepad.exe data.txt")
    except Exception as e:
        messagebox.showerror("Error", f"Nu s-a putut deschide fișierul. Detalii: {e}")

# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas= Canvas(width=200, height=200)
locker_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=locker_img)
canvas.grid(row=0, column=1)
#Labels
website_label=Label(text="Website:")
website_label.grid(row=1, column=0)

email_user_label= Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)

password_label= Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry= Entry(width=35)
website_entry.grid(row=1 ,column= 1, columnspan=2, sticky="ew")
website_entry.focus()

email_user_entry= Entry(width=35)
email_user_entry.grid(row=2, column= 1, columnspan=2, sticky="ew")
email_user_entry.insert(0, "matei@gmail.com")

password_entry=Entry(width=21)
password_entry.grid(row=3 ,column=1, sticky="ew")

#Buttons
generate_button=Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="ew")

add_button= Button(text="Add",width=36, command=add_button_click)
add_button.grid(row=4, column=1,columnspan=2,sticky="ew")

show_data_button= Button(text='Saved Passwords', command=show_data)
show_data_button.grid(row=5 ,column=2 )


window.mainloop()