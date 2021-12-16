
  #Simple calculator for converting hourly pay to an annual salary. I haven't been able to find an online calculator that does all this.
  
import tkinter as tk
from math import *

def budget(Monthlypay):
    tk.Label(text='Monthly Take Home Pay ' + str(Monthlypay)).pack()
    tk.Label(text='Hourly Pay ' + str(round(Monthlypay/160,2))).pack()
    tk.Label(font=16, text='Budget ').pack()
    tk.Label( text='Monthly Pay: ' + str(Monthlypay)).pack()
    tk.Label( text='Maximum Rent: ' + str(round(Monthlypay*.3,2))).pack()
    tk.Label( text='Monthly Utilities: ' + str(round(Monthlypay*.1,2))).pack()
    tk.Label(text='Monthly Transportation Cost : ' + str(round(Monthlypay * .2, 2))).pack()
    tk.Label(text='Monthly Spending Money: ' + str(round(Monthlypay * .1, 2))).pack()
    tk.Label(text='Monthly Student Loans: ' + str(round(Monthlypay * .15, 2))).pack()
    tk.Label(text='Monthly Groceries: ' + str(round(Monthlypay * .05, 2))).pack()

def calculate(event):
    Salary = int((entry.get()))
    Monthlypay = Salary*.85*.083 # Estimated taxes
    res.configure(  text="Maximum House Mortgage: " + str(4*Salary))
    budget(Monthlypay)


w = tk.Tk()
w.title("Mindy's Budget Calculator")
tk.Label(w, text="Enter Annual Salary:", font=16).pack()
#tk.Label(w, text="                                              ", font=16).pack()
entry = tk.Entry(w)
entry.bind("<Return>", calculate)
entry.pack()
res = tk.Label(w)
res.pack()
w.mainloop()
