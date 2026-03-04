import pandas as pd #a csv maker tool adapt as needed
l = []
dl = []
with open('cardlistpm.txt','r') as file:
	for line in file:
		l.append(line.strip("\n"))
with open('pack.txt','r') as file:
	for line in file:
		l.append(line.strip("\n"))
for i in range(0, len(l)-1):
	d = {'id': i, 'card':l[i]}
	dl.append(d)
df = pd.DataFrame(dl)
df.to_csv('packlistoff.csv', index=False)
