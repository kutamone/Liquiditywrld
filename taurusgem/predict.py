#see if we can make one that projects expenses for the year, stores previous date and moves forward off of it
#read from expenses file, if none make try, except error catching
import datetime

incomem = 250
expensesm = int(input("Month expenses: "))
monthdays = 30
dayp = 3#int(str(datetime.datetime.now())[8:10])
dayr = monthdays - dayp
ier = incomem / expensesm
print(f"Projected profit margin for the month: ${incomem - expensesm}")
print(f"Income to expense ratio for monthly purchases: ${ier}")
print(f"Earnings per day: {incomem / 30}")
print(f"Expenses per day: {expensesm / 30}")

