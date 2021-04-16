
  #Simple calculator for converting hourly pay to an annual salary. I haven't been able to find an online calculator that does all this.

def Gen_budget(budget):
    print ("************************************************ ")
    print ("General budget ")
    print ("************************************************ ")
    monthly_pay = budget/12
    print ("Monlthy Pay:                "  + str(round(monthly_pay,2)) )
    print ("Maximum Rent:               "  + str(round(monthly_pay*.30,2)) )
    print ("Maximum Utilities:          "  + str(round(monthly_pay*.10,2)) )
    print ("Maximum Transportion Cost:  "  + str(round(monthly_pay*.20,2)) )
    print ("Maximum Spending Money:     "  + str(round(monthly_pay*.10,2)) )
    print ("General Savings:            "  + str(round(monthly_pay*.15,2)) )
    print ("Student Loans:              "  + str(round(monthly_pay*.05,2)) )
    print ("Groceries:                  "  + str(round(monthly_pay*.10,2)) )

def Gen_mortage(pay):
    print ("************************************************ ")
    print ("General Mortage Calculator ")
    print ("************************************************ ")
    Home_Cost = pay * 4
    print ("House Price Estimate "  + str(round(Home_Cost,2)) )
    print ("Note: For a 30 year mortage, house payment is less than rent")

def Gen_pay(rate):
    annual_hours = 2080.00
    annual_rate = rate*annual_hours
    print ("************************************************ ")
    print ("Annual Salary")
    print ("************************************************ ")
    print ("Annual pre-tax pay :        "  + str(annual_rate) )
    average_take_home_pay = .85
    after_taxes = float(annual_rate* average_take_home_pay)
    print ("Annual post-tax pay :       "  + str(after_taxes))
    Gen_budget(annual_rate)
    Gen_mortage(annual_rate)

print('What is the hourly rate?')
hourly_rate = int(input())
Gen_pay(hourly_rate)
