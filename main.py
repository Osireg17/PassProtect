import random
import string
import tkinter
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()"+ string.ascii_uppercase + string.ascii_lowercase)
def generate():
    random.shuffle(characters)
    
    password = []
    for i in range(5,20):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    New_password = "".join(password)
    
    email_data = email_username_entry.get()
    website_data = website_entry.get()
    
    verify = messagebox.askyesno(title="Verification", message=f"Is this information correct for:\n Website: {website_data}\n Email/Username: {email_data}\n Password: {New_password}")
    
    if len(website_data) > 0 and verify == True:
        with open("data.txt","a") as data_file:
            data_file.write(f"Website: {website_data} | Email/Username: {email_data} | Password: {New_password}\n")
            website_entry.delete(0, END)
            messagebox.showinfo(title="Saved", message="Your data has been saved :)")
    else:
        messagebox.showerror(title="Invalid", message="The length of the website is too short")
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email_data = email_username_entry.get()
    password_data = password_entry.get()
    website_data = website_entry.get()
    
    verify = messagebox.askyesno(title="Verification", message=f"Is this information correct for:\n Website: {website_data}\n Email/Username: {email_data}\n Password: {password_data}")
    if len(website_data) and len(password_data) > 0  and verify == True:
        with open("data.txt", "a") as data_file:
            data_file.write(f"Website: {website_data} | Email/Username: {email_data} | Password: {password_data}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
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

window.mainloop()