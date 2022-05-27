import random
from re import search
import string
import tkinter
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()"+ string.ascii_uppercase + string.ascii_lowercase)
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error!", message="Data Not Found")
    else:
        if website in data:
            email = data[website]["email"]
            password= data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPasswords: {password}")
        else:
            messagebox.showerror(title="Error!", message=f"No details for {website} exists")
def generate():
    random.shuffle(characters)
    
    password = []
    for i in range(5,20):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    New_password = "".join(password)
    
    email_data = email_username_entry.get()
    website_data = website_entry.get()
    password_entry.insert(0, New_password)
    
    new_data = {
        website_data: {
            "email": email_data,
            "password": New_password,
    }}
    
    
    verify = messagebox.askyesno(title="Verification", message=f"Is this information correct for:\n Website: {website_data}\n Email/Username: {email_data}\n Password: {New_password}")
    
    if len(website_data) > 0 and verify == True:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:   
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            data.update(new_data)
             
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            messagebox.showinfo(title="Saved", message="Your data has been saved :)")
    else:
        messagebox.showerror(title="Invalid", message="The length of the website is too short")
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email_data = email_username_entry.get()
    password_data = password_entry.get()
    website_data = website_entry.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data,
    }}
    
    verify = messagebox.askyesno(title="Verification", message=f"Is this information correct for:\n Website: {website_data}\n Email/Username: {email_data}\n Password: {password_data}")
    
    if len(website_data) and len(password_data) > 0  and verify == True:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:   
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            data.update(new_data)
             
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            messagebox.showinfo(title="Saved", message="Your data has been saved :)")
    else:
        messagebox.showerror(title="Invalid", message="The length of the website and password are too short")
    
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

window = Tk()
#window.geometry('1000x1000+500+500')# in this line i am setting up the geometry of the window
window.title("MyPass")
window.resizable(width=False, height=False)#This is allowing me to resize the window
window.config(padx=50, pady=50)

title_label = Label(text="Pass Protect", font=("Times" , 24))
Canvas1 = Canvas(width=200, height= 200)
lock = PhotoImage(file="logo.png")
Canvas1.create_image(100,100,image=lock)
Canvas1.grid(row=0, column=1)

generate_password = Button(text='Generate Password', command=generate)
generate_password.grid(row=3, column=2)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0,"osireg@hotmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1,)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=5, column=1, columnspan=2)

search_button = Button(text="Search", width=36, command=find_password)
search_button.grid(row=6, column=1, columnspan=2)

window.mainloop()