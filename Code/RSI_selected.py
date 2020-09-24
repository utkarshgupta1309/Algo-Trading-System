#=======TEMPLATE==================
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("RSI")
width = 500
height =400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
#==================================
def info_RSI():
    root1 = Tk()
    root1.title("Know More")
    width = 600
    height =400
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

    lbl_title = Label(Top, text = "Know more about RSI", font=('arial', 15))
    lbl_title.pack(fill=X)

    T = Text(root1, height=80, width=120)
    T.pack()
    head = """RELATIVE STRENGTH INDEX(RSI)\n\n """
    quote = """RSI is a trend following indicator.
    It works on all the markets like the equality market,
    commodity market, forex market, futures market, etc.
    It shows the market condition of whether
    the market is overbought and oversold.\n
    It is a momentum oscillator. It oscillates between 0-100.

    RSI calculation formula:-
    RSI = 100 – 100 / ( 1 + RS )
    RS = Relative Strength = AvgU / AvgD
    AvgU = average of all up moves in the last N price bars
    AvgD = average of all down moves in the last N price bars
    N = the period of RSI

    RSI DEFAULT SETTING:-
    14 days or many traders use days between 9 to 14 days.

    The time frame chart for RSI is 5 min or 10 min for trading.

    RSI Divergences
    A trader might buy when price and the Relative Strength Index are both rising and the RSI crosses above the 50 Line.
    Similarly, a trader might sell when the price and the RSI are both falling and the RSI crosses below the 50 Line.

    RSI between 30-70(daily chart)
    when RSI is 30 and bounce back just below the 30 it means buying signal is generated.
    and when RSI is at 70 and due to resistance at 70 or just above it slowly moves downward it means selling signal is generated.
    RSI between 50-100(daily chart)\n
    when RSI takes support at 50 and also move above 70 slowly it means a long bullish trend.
    RSI between 50-0(daily chart)\n
    If RSI takes resistance at 50 and also moves down 30 slowly it means a long bearish trend.
    RSI between 70-100(daily chart)\n
    If RSI takes support at 70 then it means a strong bullish trend.
    RSI between 30-0(daily chart)\n
    If RSI takes resistance at 30 it means a strong bearish trend."""
    T.insert(END, head)
    T.insert(END, quote)




#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=300)
Form.pack(side=TOP, pady=20)

#==============================LABELS=========================================
lbl_title = Label(Top, text = "Configure RSI", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_info = Button(Top, text = "Know more", font=('arial', 10),width =1, command = info_RSI)
lbl_info.pack(fill=X)
lbl_name = Label(Form, text = "Enter the period of RSI", font=('arial', 14), bd=15)
lbl_name.grid(row=0, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=4, columnspan=5)
#==============================ENTRY WIDGETS==================================
PERIOD = StringVar()
name = Entry(Form, textvariable=PERIOD, font=(14))
name.grid(row=1, column=0)
#===============Buttons=================================
btn_submit= Button(Form, text="Submit", width=45)
btn_submit.grid(pady=25, row=5, columnspan=2)

root.mainloop()
