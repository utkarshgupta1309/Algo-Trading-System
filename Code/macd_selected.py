
#=======TEMPLATE==================
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("MACD")
width = 500
height =600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
#==================================
def info_MACD():
    root1 = Tk()
    root1.title("Know More")
    width = 500
    height =600
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root1.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root1.resizable(0, 0)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    Top = Frame(root, bd=2,  relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(root, height=300)
    Form.pack(side=TOP, pady=20)

    lbl_title = Label(Top, text = "Know more about MACD", font=('arial', 15))
    lbl_title.pack(fill=X)

    T = Text(root1, height=80, width=40)
    T.pack()
    quote = """MACD is a trend following indicator. it is made with the combination of two different EMA.

    MACD CALCULATION:-
    The MACD is calculated by subtracting the 26-period Exponential Moving Average (EMA) from the 12-period EMA.
    The result of that calculation is the MACD line. A nine-day EMA of the MACD called the "signal line," is then plotted on top of the MACD line, which can
     function as a trigger for buy and sell signals.

    MACD DEFAULT SETTING:-
    12,26,9
    where 12 indicate MACD line, 26 indicate the SIGNAL line and 9 indicate MACD histogram.

    The time frame chart for MACD is 5 min or 10 min.

    MACD CROSSOVER
    A possible buy signal is generated when the MACD (blue line) crosses above the zero line."""
    T.insert(END, quote)




#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=300)
Form.pack(side=TOP, pady=20)

#==============================LABELS=========================================
lbl_title = Label(Top, text = "Configure MACD", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_info = Button(Top, text = "Know more", font=('arial', 10),width =1, command = info_MACD)
lbl_info.pack(fill=X)
lbl_name = Label(Form, text = "Enter number of periods to calculate the\n faster-moving average.", font=('arial', 14), bd=15)
lbl_name.grid(row=0, sticky="e")
lbl_date = Label(Form, text = "Enter number of periods to calculate the \nslower moving average.", font=('arial', 14), bd=15)
lbl_date.grid(row=2, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=4, columnspan=5)
#==============================ENTRY WIDGETS==================================
FMA = StringVar()
SMA= StringVar()
name = Entry(Form, textvariable=FMA, font=(14))
name.grid(row=1, column=0)
date = Entry(Form, textvariable=SMA, font=(14))
date.grid(row=4, column=0)
#===============Buttons=================================
btn_submit= Button(Form, text="Submit", width=45)
btn_submit.grid(pady=25, row=5, columnspan=2)

root.mainloop()
