#Google Gemini 3 Hackathon
#2d world - finance - yugioh
#random
import random
#csv
import csv
#mine
from tabul import dataview
from cashview import transact, tview, tview2, finput
from cudraw import cud
#pandas
import pandas as pd
#matplotlib
import matplotlib.pyplot as plt
#datetime
import datetime
from datetime import date
#pygame: coordinates and Keybinding
import pygame
#tkinter
import tkinter as tk
from tktut import window
#gemini
#pygame
pygame.init()
screen = pygame.display.set_mode((972,972))

pygame.display.set_caption('map')
bg = pygame.image.load('twnmap.png').convert_alpha()
char = pygame.image.load('guy1-441e.png').convert_alpha()
font = pygame.font.Font('freesansbold.ttf', 24)
blk = (0,0,0)

#functions
def cardlistread():
	cl = []
	with open('cardlistpc.txt', 'r') as f:
		for line in f:
			cl.append(line.strip('\n'))
	return cl
def cardrefill():
	bitl = []
	clm = []
	with open('bits.txt', 'r') as file:
		for line in file:
			bitl.append(int(line))
	with open('bits.txt', 'w') as file:
		file.write(str(bitl[0] - 2500))
	with open('cardlistpm.txt', 'r') as cf:
		for line in cf:
			clm.append(line)
	with open('cardlistpc.txt', 'w') as cf:
		for x in clm:
			cf.write(f"{x}")
	print("Full Cards Back!")
	print("2500 bits exchanged \n")
	with open('cardlistpc.txt','r') as file:
		for line in file:
			print(line)
def fhouse():
	data = []
	with open('finances.csv', 'r') as file:
		csvr = csv.DictReader(file)
		for row in csvr:
			data.append(row)
	with open('finances2.csv', 'r') as file:
		csvr2 = csv.DictReader(file)
		for row in csvr2:
			data.append(row)
	with open('finances3.csv', 'r') as file:
		csvr3 = csv.DictReader(file)
		for row in csvr3:
			data.append(row)
	with open('fproject.csv', 'r') as file:
		csvr4 = csv.DictReader(file)
		for row in csvr4:
			data.append(row)
	print(dataview(data[0]))
	print(dataview(data[1]))
	print(dataview(data[2]))
	print("\n Manual Projections: \n")
	print(dataview(data[3]))
	tview() 
def cardshop():
	bitl = []
	cardadd = []
	cardl = []
	cardlpc = []
	with open('cardshopl.csv', 'r') as file:
		for line in file:
			cardl.append(line.strip('\n'))
		x = random.randint(0,len(cardl))
		cardadd.append(cardl[x])
	with open('cardlistpc.txt', 'r') as file:
		for line in file:
			cardlpc.append(line)
		cardlpc.append(cardadd[0]+'\n')
	with open('cardlistpc.txt', 'w') as file:
		for x in cardlpc:
			file.write(f"{x}")
	with open('bits.txt', 'r') as file:
		for line in file:
			bitl.append(int(line))
	with open('bits.txt', 'w') as file:
		file.write(str(bitl[0] - 250))
	print("Random card added to cardlist!")
	print(cardadd)
	print("250 bits exchanged \n")
	
def gameover():
	bitsl = []
	with open('bits.txt', 'r') as file:
		for line in file:
			bitsl.append(int(line))
	if bitsl[0] <= 0:
		print("GAME OVER")
		pygame.quit()
	else:
		pass
def npclines():
	npcl = []
	with open('npclines.txt', 'r') as file:
		for line in file:
			npcl.append(line)
	x = random.randint(0,len(npcl)-1)
	print("____________")
	print(npcl[x] +"\n")
	print("-------------")
def qvshow():
	quiz1 = []
	pts = 0
	with open('v.csv', 'r') as file:
		csvr = csv.DictReader(file)
		for row in csvr:
			quiz1.append(row)
	a1 = input(f"{quiz1[0]['Question']} (y/n)")
	if a1 == 'y':
		pts += 1
	a2 = int(input(f"{quiz1[1]['Question']} \n: "))
	pts += a2
	a3 = int(input(f"{quiz1[2]['Question']} \n: "))
	pts += a3
	if a2 >= 5 or a3 <= 10:
		print("Keep up the good work! \n")
		pack()
	else:
		print("Try harder next time to stick to your goals")
	with open('vview.csv', 'a') as vv:
		vv.write(f"{datetime.datetime.now()},{pts}\n")
def vhouse():
	view1l = []
	with open('vview.csv', 'r') as file:
		csvr = csv.DictReader(file)
		for row in csvr:
			view1l.append(row)
	for i in range(0,len(view1l)): 	
		print(dataview(view1l[i]))
		
def pack():
	print("You got a new pack!")
	packl = []
	cardlpc = []
	with open('pack.txt', 'r') as file:
		for line in file:
			packl.append(line.strip('\n'))
		z = random.randint(0,len(packl)-1)
	with open('cardlistpc.txt', 'r') as file:
		for line in file:
			cardlpc.append(line)
		print(f"New card added: {packl[z]}")
		cardlpc.append(packl[z]+'\n')
	with open('cardlistpc.txt', 'w') as file:
		for x in cardlpc:
			file.write(f"{x}")
def phouseview():
	print("Systems for progression based on input")
	proglog = []
	with open('plist.csv','r') as file:
		csvr = csv.DictReader(file)
		for line in csvr:
			proglog.append(line)
	print("-------Tasks------(1 = complete)")
	for dictio in proglog:
		print(f"{dictio['Task']} {dictio[' Completion Status']}")
def phouse():
	print("Systems for progression based on input")
	proglog = []
	proglist = []
	with open('plist.csv','r') as file:
		csvr = csv.DictReader(file)
		for line in csvr:
			proglog.append(line)
		for i in proglog:
			print(f'{i} {proglog.index(i)}')
		edit = int(input("Which task was completed? \nEnter the number next to the line of the task\n :"))
		proglog[edit][' Completion Status'] = 1
		df = pd.DataFrame(proglog)
		df.to_csv("plist.csv", index=False) #pandas takes dictionaries and converts it back to csv
			
		pack()
def dungeon():
	nothing = "The dungeon was normal today"
	taunt = "Press d right now you won't"
	dx = random.randint(0,4)
	if dx == 3:
		pack()
	elif dx == 2:
		print(taunt)
	else:
		print(nothing)
def stockh():
	plstock = []
	rc = random.choice(['UP','DOWN','STEADY'])
	with open('pack.txt','r') as file:
		for line in file:
			plstock.append(line)
	r = random.randint(0,len(plstock)-1)
	print("\n=================\n")
	print(f"Rare Card Announcement: {plstock[r]} -+- STOCK {rc}")
	print("=================\n")	
def exp():
	expd = [{'exp': 0,'level': 0}]
	expr = []
	with open('exp.csv','r') as file:
		csvr = csv.DictReader(file)
		for line in csvr:
			expr.append(line)
	expr[0]['exp'] = int(expr[0]['exp'])
	expr[0]['exp'] += 250
	print("\n\n==========You Gained  250 EXP=============\n")
	if expr[0]['exp'] % 2000 == 0:
		print("\n\n=============LEVEL UPPPPP=============")
		expr[0]['level'] = int(expr[0]['level'])
		expr[0]['level'] += 1
		print(f"============{expr[0]['level']}===============")
		pack()
	df = pd.DataFrame(expr)
	df.to_csv('exp.csv',index = False)
def lvlshow():
	with open('exp.csv','r') as file:
		csvr = csv.DictReader(file)
		for line in csvr:
			print(line)
def currbonus():
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
						print("CONGRATULATIONS YOU SPENT $0 TODAY")
						print("You Gain EXP and a pack")
						exp()
						pack()
			with open('dat.csv','a') as d:
				d.write(f',{timenow}\n')
				if timenow in i[0:10]:
					with open('dat.csv','a') as d:
						d.write(f'1')
						print("You redeemed your bonus for the day")
						print("You Do Not Gain EXP") #subtracts the total gained to make 0
		if datl and datl[0]['date'] != timenow:
			with open('dat.csv','w') as d:
				d.write("switch,date\n")
				for i in llist:
					zstring += '0'
				d.write(f"{zstring},{timenow}\n")
			print("CONGRATULATIONS YOU SPENT $0 TODAY")
			print("You gain EXP and a pack")
			exp()
			pack()
		else:
			print("You already redeemed your exp bonus for the day")
#tkinter functions
def draw(cardlist):
	root = tk.Tk()
	root.title("Battle")
	root.geometry("700x600")
	label = tk.Label(root, text = "You have been challenged to a duel by John")
	
	x = random.randint(0,len(cardlist)-1)
	z = random.randint(0,10)
	c = random.randint(0,10)
	p = random.randint(0,len(cardlist)-1)
	
	if cardlist[x] == "Celestial Dragon":#mods where dragons are OP
		z = 8
	if cardlist[x] == "Purple Eyes Dragon":
		z = 8
	
	label2 = tk.Label(root, text = cardlist[x])
	label3 = tk.Label(root, text = f"{z} vs {c}")
	label4 = tk.Label(root, text = cardlist[p])
	label.pack(pady = 10)
	label2.pack(pady = 25)
	label3.pack(pady = 30)
	label4.pack(pady = 50)
	
	btn = tk.Button(root, text = "Close", command = root.destroy)
	btn.pack()
	root.mainloop()
	
	if z > c:
		print("You won the duel!")
		print("You get 500 bits")
		bitl = []
		with open('bits.txt', 'r') as file:
			for line in file:
				bitl.append(int(line))
		with open('bits.txt', 'w') as file:
			file.write(str(bitl[0] + 500))
	else:
		print("You lost to John!")
		cardlist.remove(cardlist[-1])
		with open('cardlistpc.txt', 'w') as file:
			for x in cardlist:
				file.write(f"{x}\n")
		print("You lost a card!")
def fwindow(kl, vl):
	root = tk.Tk()
	root.title("Finance View")
	root.geometry("400x300")
	label = tk.Label(root, text= f"{kl}")
	label2 = tk.Label(root, text= f"{vl}")
	label.pack(pady = 15)
	label2.pack(pady = 20)
	btn = tk.Button(root, text = "Close", command = root.destroy)
	btn.pack()
	root.mainloop()
#matplotlib functions
def fplot(listx, listy):
	plt.figure(figsize=(8,5))
	plt.plot(listx, listy, color = 'blue')
	plt.xlabel('Finances')
	plt.ylabel('Cash')
	plt.title('Finance View')
	plt.grid(axis='y', linestyle= '--', alpha=0.7)
	plt.show()
#variables
bitslm = []
data = []
kl = []
vl = []
vlint = []
charx = 360
chary = 325
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#read/write operations
with open('bits.txt','r') as file:
	for line in file:
		bitslm.append(line + ' b')
with open('finances3.csv', 'r') as file:
	csvr = csv.DictReader(file)
	for row in csvr:
		data.append(row)
	kl += list(data[0].keys())
	vl += list(data[0].values())
	for i in range(len(vl)):
		vlint.append(int(vl[i]))
#renders
bitrender = font.render(bitslm[0], True, 'white')
h1name = font.render('Finance House', True, 'white')
h2name = font.render('Card Shop', True, 'white')
h3name = font.render('Vest House', True, 'white')
h4name = font.render('Progression House', True, 'white')
h5name = font.render('Dungeon', True, 'white')
h6name = font.render('Stock Market House', True, 'white')

run = True
while run:
	screen.fill(blk)
	
	mx, my = pygame.mouse.get_pos()
	
	screen.blit(bg, (0,-20))
	screen.blit(char, (mx, my))
	screen.blit(bitrender, (40,40))
	
	screen.blit(h1name, (106,227))
	h1 = pygame.Rect(245,309,50,50)
	#pygame.draw.rect(screen, blk, (245,309,50,50))#h1
	
	screen.blit(h2name, (267,149))
	h2 = pygame.Rect(369,233,50,50)
	#pygame.draw.rect(screen, blk, (369,233,50,50))#h2
	
	screen.blit(h3name, (439,53))
	h3 = pygame.Rect(475,141,50,50)
	#pygame.draw.rect(screen, blk, (475,141,50,50))#h3
	
	screen.blit(h4name, (584,142))
	h4 = pygame.Rect(601,214,50,50)
	#pygame.draw.rect(screen, blk, (601,214,50,50))#h4
	
	screen.blit(h5name, (733,199))
	h5 = pygame.Rect(731,294,50,50)
	#pygame.draw.rect(screen, blk, (731,294,50,50))#h5
	
	screen.blit(h6name, (560,455))
	h6 = pygame.Rect(573,536,50,50)
	#pygame.draw.rect(screen, blk, (573,536,50,50))#h6
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				chary -= 10
			if event.key == pygame.K_DOWN:
				chary += 10
			if event.key == pygame.K_RIGHT:
				charx += 10
			if event.key == pygame.K_LEFT:
				charx -= 10
			if event.key == pygame.K_RSHIFT:
				numcards = []
				print("--------Cardlist---------")
				with open('cardlistpc.txt','r') as file:
					for line in file:
						numcards.append(line)
						print(line)
				print(f"You have {len(numcards)} cards")
			if event.key == pygame.K_LSHIFT:
				transact()
			if event.key == pygame.K_s:
				dt = str(datetime.datetime.now())
				with open('savedate.txt', 'w') as f:
					f.write(dt)
				print("Welcome to Liquidity World!")
				print(f"Today is {dt}")
				dtl = list(dt)
				if dtl[8] == str(1) and dtl[9] == str(3): #13th of the month
					 print("Special Pack Opening Day today on the 13th!")
					 pack()
				today = datetime.datetime.today()
				if today.weekday() >= 5:
					print("It's the weekend, let's check if we should spend or save today")
					pack()
				currbonus()
			if event.key == pygame.K_d:
				try:
					draw(cardlistread())		
				except ValueError as e:
					print("Err..or de..tected..")
					print(f"{e} YOU LOST ALL YOUR CARDSSS!")
			if event.key == pygame.K_c:
				cardrefill()
			if event.key == pygame.K_f:
				fplot(kl, vlint)
			if event.key == pygame.K_v:
				tview2()
			if event.key == pygame.K_q:
				qvshow()
			if event.key == pygame.K_t:
				phouse()
			if event.key == pygame.K_a:
				transact()
			if event.key == pygame.K_e:
				finput()
		if event.type == pygame.MOUSEBUTTONDOWN:
			print("Click")
			print(f"Mouse pos: {mx},{my}")
			lvlshow()
			print(bitslm)
			
			if h1.collidepoint(mx, my):
				print("Finance House")
				fhouse()
				exp()
				gameover()
				
			if h2.collidepoint(mx, my):
				print("Card Shop")
				print("250 bits for a card")
				cardshop()
				gameover()
				
			if h3.collidepoint(mx, my):
				print("Vest House")
				print("Press q for the quiz to earn a pack \n")
				print("Here are your previous quiz results: ")
				vhouse()
				exp()
				
			if h4.collidepoint(mx, my):
				print("Progression House")
				print("Press t to update task completion")
				phouseview()
				exp()
				
			if h5.collidepoint(mx, my):
				print("Dungeon")
				dungeon()
	
			if h6.collidepoint(mx, my): #ai
				print("Stock Market House")
				stockh()
						
		if event.type == pygame.MOUSEBUTTONUP:
			npclines()
		if event.type == pygame.MOUSEWHEEL:
			print(f"Wheel scroll: {event.x}, {event.y}")
		gameover()
		
	pygame.display.update()
pygame.quit()
