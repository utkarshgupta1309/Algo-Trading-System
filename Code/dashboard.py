import sys
import os
from tkinter import *
import sqlite3
root = Tk()
root.title("Algorithm Trading System")
width = 800
height =600
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
lbl_title = Label(Top, text = "Welcome\n", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_title = Label(Top, text = "Dashboard", font=('arial', 12))
lbl_title.pack(fill=X)


#======================integrating Funtion=========================
def getStocks():
    os.system('getstocks.py')
#=============================Buttons=============================
# lbl_title = Label(root, text = "Dashboard", font=('arial', 12))
# lbl_title.pack(fill=X)
photo = PhotoImage(file = "tenor.gif")

#build_strat_icon = build_strat.subsample(1, 1)
photoimage = photo.subsample(1, 1)
build_img= Button(root, text="View Account", image = photo,compound = LEFT).pack(side = TOP)
build_img= Button(root, text="Get Stocks", image =photo,compound = LEFT,command = getStocks).pack(side = TOP)
build_img= Button(root, text="View Strategy", image = photo,compound = LEFT).pack(side = TOP)

if __name__ == '__main__':
    root.mainloop()
