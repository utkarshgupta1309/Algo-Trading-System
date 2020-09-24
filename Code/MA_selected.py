#=======TEMPLATE==================
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Moving Average")
width = 500
height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
#==================================

#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)

#==============================LABELS=========================================
lbl_title = Label(Top, text = "Configure Moving Average", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_name = Label(Form, text = "Enter number of periods to calculate the Moving average for", font=('arial', 14), bd=15)
lbl_name.grid(row=0, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=4, columnspan=5)
#==============================ENTRY WIDGETS==================================
MA = StringVar()
name = Entry(Form, textvariable=MA, font=(14))
name.grid(row=1, column=0)
#===============Buttons=================================
btn_submit= Button(Form, text="Submit", width=45)
btn_submit.grid(pady=25, row=5, columnspan=2)





root.mainloop()
