import csv
import datetime
import pandas as pd
from tabul import dataview
import matplotlib.pyplot as plt
def transact():
	list1 = []
	tran = int(input("Number of transactions: "))
	i = 0
	while i < tran:
		mkey = input("Enter a transaction name: ")
		mval = int(input("Enter the transaction amount: "))
		date = str(datetime.datetime.now())[0:10]
		with open('fmonth1.csv', 'a') as file:
			file.write(f"{date},{mkey},{mval} \n")
		with open('fmonth1.csv', 'r') as file:
			csvr = csv.DictReader(file)
			for row in csvr:
				list1.append(row)
			for x in range(0,len(list1)):
				for y in list1[x]:
					if y == 'Cost':
						list1[x][y] = float(list1[x][y]) #reassign cost values to float for all item in list
		i+=1
def tview():
	list1 = []
	list2 = []
	with open('fmonth1.csv', 'r') as file:
		csvr = csv.DictReader(file)
		for row in csvr:
			list1.append(row)
		for i in range(0,len(list1)):
			list2.append(int(list1[i]['Cost']))
		x = sum(list2)
		frame = pd.DataFrame(list1)
		print("Your transactions for your main account (fmonth1.csv): \n")
		print(frame)
		print(f"\n Total extra expenses for the current month: {x} \n")
		print(f"\n Total Overall expenses for the current month: {x+55} \n")
		
		currex = x+55 #note expenses locked at 55 per month
		dayp = int(str(datetime.datetime.now())[8:10])
		monthdays = 30
		dayr = monthdays - dayp
		#print(dayp, dayr, currex)
		if dayr < 0:
			monthdays += 1
			dayr = monthdays - dayp	
		
		res = ((currex / dayp) * dayr) + currex
		prevmonthex = 227.5 #average of last two months expenses
		print(f"You are projected to spend $ {prevmonthex} this month")
		print(f"Your current expected profit margin is ${250 - prevmonthex}")#note income locked at 250 #used to be 250 - res
		
		if dayr <= 2 and dayr > 0: #3 for the demo
			sugg = input("Would you like to save this month's transactions to a file? (y/n) :")
			if sugg == "y":
				with open('monthreview.csv', 'w') as m:
					profitl = f"Your net profit for the last month was ${250-res}"
					expensel = "Your expenses were as follows: "
					for line in list1:
						file.write(f"{line}\n")
				print("Your month's transactions were written to monthreview.csv")
		else:
			print("Viewing information")
				
		
def tview2():
	list1 = []
	list2 = []
	list3 = []
	with open('fmonth1.csv', 'r') as file: #modify this line to change the monthly view
		csvr = csv.DictReader(file)
		for row in csvr:
			list1.append(row)
		for i in range(0,len(list1)):
			list2.append(int(list1[i]['Cost']))
		x = sum(list2)
		for i in range(0,len(list1)):
			list3.append(list1[i]['Date'])
		plt.figure(figsize=(8,5))
		plt.plot(list3, list2, color = 'blue')
		plt.xlabel('Date')
		plt.ylabel('Cost')
		plt.title('Finance View')
		plt.grid(axis='y', linestyle= '--', alpha=0.7)
		plt.show()
def finput():
	choos = input("Would you like to edit savings numbers, monthly numbers or weekdays? [Enter 1, 2, or 3]")
	if choos == '1':
		print("Enter your Savings, Spending, Equity and Investments: ")
		f1 = [int(input(": ")) for i in range(0,4)]
		d1 = [{
		'Savings':f1[0],
		'Spending':f1[1],
		'Equity':f1[2],
		'Investments':f1[3]	
		}]
		df = pd.DataFrame(d1)
		df.to_csv('finances.csv', index = False)
	if choos == '2':
		print("Enter your Monthly Income and Monthly Expenses")
		f2 = [int(input(": ")) for i in range(0,2)]
		d2 = [{
		'Monthly Income': f2[0],
		'Monthly Expenses': f2[1],
		'Profit Margin': (f2[0] - f2[1])
		}]
		df2 = pd.DataFrame(d2)
		df2.to_csv('finances2.csv', index = False)
	if choos == '3':
		choos2 = int(input("How many days would you like to show? "))
		d3 = {input("Enter your weekday: ") : int(input("How much did you spend on this day: ")) for i in range (0,choos2)}#now only shows selected days on which you spent money instead of every day
		df3 = pd.DataFrame([d3])
		df3.to_csv('finances3.csv', index = False)	
def projectmt():
	curr = int(input("Current expenses for month: "))
	dayp = int(input("Days passed in month: "))
	dayr = int(input("Days in month remaining: "))

	res = ((curr / dayp) * dayr) + curr
	print(f"You are projected to spend $ {res} this month")
