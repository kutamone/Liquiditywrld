a = [1,1,1,2,2,2,2,2,3,3,4,5]
def cardcheck(l):
	dl = []
	b = set()
	for i in a:
		b.add(i) 
	for i in b:
		d = {i : l.count(i)}
		dl.append(d)
	return dl
print(cardcheck(a))  
