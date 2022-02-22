# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
from turtle import width, window_width
from PIL import ImageTk, Image
from random import *

from matplotlib.pyplot import text
from pyparsing import White

window = Tk()
#window.geometry('1000x1000+500+500')# in this line i am setting up the geometry of the window
window.title("MyPass")
window.resizable(width=True, height=True)#This is allowing me to resize the window
window.config(padx=20, pady=20, bg='#FFDEAD')

title_label = Label(text="Pass Protect", font=("Times" , 24))
Canvas1 = Canvas(width=200, height= 200,background="#FFFFFF")
lock = PhotoImage(file="logo.png")
Canvas1.create_image(100,100,image=lock)
Canvas1.grid(row=1, column=3)

generate_password = Button(text='Generate Password', padx=10)
generate_password.grid_configure(row=7, column=4)

website_label = Label(text="Website: ", width=20)
website_label.grid_configure(row=4, column=1)

website_entry = Entry(width=35)
website_entry.grid_configure(row=4, column=2, columnspan=2)

email_username_label = Label(text="Email/Username", width=20)
email_username_label.grid_configure(row=5, column=1)

email_username_entry = Entry(width=35)
email_username_entry.grid_configure(row=5, column=2, columnspan=2)

password_label = Label
password_entry = Entry(width=21)

window.mainloop()