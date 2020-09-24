import sys
import os
import Cale
DATE = Cale.ret()
print(DATE)
i = 0
from tkinter import *
def calendar():
    Cale.main()
    global DATE
    global i
    DATE = Cale.ret()
    i = i+1
    build_frame()


def getstocksWindow():
    def getstocks(name,date):
        import datetime
        import pandas_datareader.data as web
        from datetime import datetime
        start = date
        end = datetime.now()

        # ======Code to download data============
        df = web.DataReader(name,'yahoo', start, end)
        RELIANCE = df.to_csv('RELIANCE.csv')
        df.reset_index(inplace=True)
        df.set_index("Date", inplace=True)
        print(df.head())
        # =====================================


    def build_frame():
        i = 0
        root = Tk()
        root.title("Algorithm Trading System")
        width = 400
        height =400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)

        #==============================FRAMES=========================================
        Top = Frame(root, bd=2,  relief=RIDGE)
        Top.pack(side=TOP, fill=X)
        Form = Frame(root, height=200)
        Form.pack(side=TOP, pady=20)

        #==============================LABELS=========================================
        lbl_title = Label(Top, text = "Pick Stocks", font=('arial', 15))
        lbl_title.pack(fill=X)
        lbl_name = Label(Form, text = "Enter the name of the stock:", font=('arial', 14), bd=15)
        lbl_name.grid(row=0, sticky="e")
        lbl_info = Label(Form, text = "Start Date",font=('arial', 14), bd=15)
        lbl_info.grid(row=2, sticky="e")
        global DATE
        if(i == 0):
            lbl_date = Label(Form, text = DATE,font=('arial', 14), bd=15)
            lbl_date.grid(row=3, sticky="e")
            lbl_text = Label(Form)
            lbl_text.grid(row=4, columnspan=5)
        else:
            lbl_date = Label(Form, text = DATE,font=('arial', 14), bd=15)
            lbl_date.grid(row=3, sticky="e")
            lbl_text = Label(Form)
            lbl_text.grid(row=4, columnspan=5)

        #==============================ENTRY WIDGETS==================================
        STOCKNAME = StringVar()
        name = Entry(Form, textvariable=STOCKNAME, font=(14))
        name.grid(row=1, column=0)

        #===============Buttons=================================
        btn_submit= Button(Form, text="Submit", width=45,command = lambda: getstocks(name.get(),DATE))
        btn_submit.grid(pady=25, row=5, columnspan=2)
        btn_calendar = Button(Form, text="Calendar", width=45,command = calendar)
        btn_calendar.grid(pady=25, row=6, columnspan=2)
        if(i != 0):
            def destroy():
                root.destroy()
                popup.destroy()

            popup = Tk()
            popup.wm_title("!")
            label = ttk.Label(popup, text="Done")
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(popup, text="Okay", command = destroy)
            B1.pack()
            popup.mainloop()
        i = i+1

        if __name__ == '__main__':
            root.mainloop()


    build_frame()
getstocksWindow()
