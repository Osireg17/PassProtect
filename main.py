# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
from turtle import window_width
from PIL import ImageTk, Image

window = Tk()
window.geometry('1000x1000+500+500')# in this line i am setting up the geometry of the window
window.title("MyPass")
window.resizable(width=True, height=True)#This is allowing me to resize the window
window.config(padx=20, pady=20, bg='#FFDEAD')

title_label = Label(text="Pass Protect", font=("Times" , 24))
Canvas1 = Canvas(width=200, height= 200)
lock = PhotoImage(file="logo.png")
lock.create_image(100,100,image=lock)
Canvas1.pack()

window.mainloop()