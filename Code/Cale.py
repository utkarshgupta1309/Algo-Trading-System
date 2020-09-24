var1 = 0
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

def main():
    top = tk.Tk()
    top.title("Date Picker")
    ttk.Label(top, text='Choose Start date').pack(padx=80, pady=40)
    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=20, pady=10)

    def date_sel():
        global var1
        var1 = cal.get_date()
    def destroy():
         top.destroy()

    ttk.Button(top, text="Select Date", command=date_sel).pack(padx=10, pady=10)
    ttk.Button(top, text="Proceed", command=destroy).pack(padx=5, pady=5)

    top.mainloop()
    return(var1)
def ret():
    return(var1)
main()
