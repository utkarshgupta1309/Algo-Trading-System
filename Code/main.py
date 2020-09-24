import sys
import os
from tkinter import *

window=Tk()

window.title("Running Python Script")
window.geometry('550x200')

def runLogin():
    os.system('interLogin.py')

btn = Button(window, text="Login", bg="black", fg="white",command=runLogin)
btn.grid(column=1, row=0)

def runDashboard():
    os.system('dashboard.py')

btn = Button(window, text="Dashboard", bg="black", fg="white",command=runDashboard)
btn.grid(column=0, row=0)

window.mainloop()