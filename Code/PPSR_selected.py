#=======TEMPLATE==================
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Pivot Points")
width = 500
height =400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
#==================================
def info_PPSR():
    root1 = Tk()
    root1.title("Know More")
    width = 500
    height =300
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

    lbl_title = Label(Top, text = "Know more about Pivot Points", font=('arial', 15))
    lbl_title.pack(fill=X)

    T = Text(root1, height=80, width=40)
    T.pack()
    quote = """PIVOT POINT LEVEL :-                                                                                                                                                                       The pivot point is a trading strategy or system that uses short timeframes and the daily pivot points.
    Pivot points are one of the most widely used indicators in day trading.
    The tool provides a specialized plot of seven support and resistance levels intended to find intraday turning points in the market.

    Calculation of Pivot Points
    Pivot points can be calculated for various timeframes in some charting software programs that allow you to customize the indicator.
    Pivot Point = [High (previous) + Low (previous) + Close (previous)] / 3

    The other six price levels – three support levels and three resistance levels – all use the value of the pivot point as part of their calculations.
    The three support levels are conveniently termed support 1, support 2, and support 3. The three resistance levels are referred to as resistance 1, resistance 2, and resistance 3. You may also see them called by their shorthand forms – S1, S2, S3, and R1, R2, R3, respectively.
    These values are calculated as follows:
    Resistance 1 = (2 x Pivot Point) – Low (previous period)
    Support 1 = (2 x Pivot Point) – High (previous period)
    Resistance 2 = (Pivot Point – Support 1) + Resistance 1
    Support 2 = Pivot Point – (Resistance 1 – Support 1)
    Resistance 3 = (Pivot Point – Support 2) + Resistance 2
    Support 3 = Pivot Point – (Resistance 2 – Support 2)

    WHEN TO BUY OR SELL
    Be bearish when the price is below the main pivot point.
    Be bullish when the price is above the main pivot point.
    Go long if the price bounces from S1, S2, or S3.
    Go short if the price bounces from R1, R2, or R3.
    If you want pivot point for tomorrow then you have to take high price, low price and close price of today.
    If you want a pivot point for next week then you have to take a high price, low price and close price of this week.
    If you want a pivot point for next month then you have to take a high price, low price and close price of this week."""
    T.insert(END, quote)




#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=300)
Form.pack(side=TOP, pady=20)

#==============================LABELS=========================================
lbl_title = Label(Top, text = "Configure Pivot points", font=('arial', 15))
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
