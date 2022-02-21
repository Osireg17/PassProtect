# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from curses import window
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('1000x1000+500+500')# in this line i am setting up the geometry of the window
window.title("MyPass")
window.resizable(width=True, height=True)#This is allowing me to resize the window
