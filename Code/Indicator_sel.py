from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Select Indicators")
width = 800
height =600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
frame = ttk.Frame(root, padding=(3, 3, 12, 12))
frame.grid(column=0, row=0, sticky=(N, S, E, W))

values = StringVar()
values.set("Moving_Average EMA MACD RSI")

lstbox = Listbox(frame, listvariable=values, selectmode=MULTIPLE, width=20, height=10)
lstbox.grid(column=0, row=0, columnspan=2)

def select():
    reslist = list()
    seleccion = lstbox.curselection()
    for i in seleccion:
        entrada = lstbox.get(i)
        reslist.append(entrada)
    for val in reslist:
        print(val)

btn = ttk.Button(frame, text="Continue", command=select)
btn.grid(column=1, row=1)

root.mainloop()
