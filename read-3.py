
txt = []
with open('3.txt' , 'r' , encoding = 'utf-8-sig') as f :
	for line in f :
		txt.append(line.strip())
for line in txt :
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print(name)
	print(time)
	print(s)
	
