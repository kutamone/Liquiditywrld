import datetime
import csv
llist = []
datl = []
zstring = ''
timenow = str(datetime.datetime.now())[0:10]
with open('dat.csv','r') as d:
	csvr = csv.DictReader(d)
	for line in csvr:
		datl.append(line)
with open('fmonthlast.csv','r') as file:
	for line in file:
		llist.append(line.strip('\n'))
	if not datl:
		for i in llist:
			if timenow not in i[0:10]:
				with open('dat.csv','a') as d:
					d.write(f'0') #there were no transactions that day
					print("You Gain EXP") #adds currency
		with open('dat.csv','a') as d:
			d.write(f',{timenow}\n')
			if timenow in i[0:10]:
				with open('dat.csv','a') as d:
					d.write(f'1')
					print("You Do Not Gain EXP") #subtracts the total gained to make 0
	if datl and datl[0]['date'] != timenow:
		with open('dat.csv','w') as d:
			d.write("switch,date\n")
			for i in llist:
				zstring += '0'
			d.write(f"{zstring},{timenow}\n")
		print("Dates not equal, file reset")
		print("You gain EXP")
	else:
		print("Date in there, so did nothing")	
		
