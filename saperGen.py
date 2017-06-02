import random
field = []
for i in range (101):
	a = ' '
	field.append(a)
a = 0
while a != 10:
	ranN = random.randint(0,100)
	if field[ranN] != '*':
		field[ranN] = '*'
		a += 1
def prin():
	for i in range (0, 91):
		b = i+10
		arrN1 = [0,10,20,30,40,50,60,70,80,90]
		for c in range (10):
			if i == arrN1[c]:
				print (field[i:b])
prin()
for i in range (101):
	if field[i] != '*':
		def standartF(a,b,c,d,e,f,g,h):
			count = 0
			if a == 1:
				if field[i-1] == '*':
					count +=1
			if b == 1:
				if field[i-11] == '*':
					count +=1
			if c == 1:
				if field[i-10] == '*':
					count +=1
			if d == 1:
				if field[i-9] == '*':
					count +=1
			if e == 1:
				if field[i+1] == '*':
					count +=1
			if f == 1:
				if field[i+11] == '*':
					count +=1
			if g == 1:
				if field[i+10] == '*':
					count +=1
			if h == 1:
				if field[i+9] == '*':
					count +=1
			return count
		arrN6 = [10,20,30,40,50,60,70,80,90,100,9,19,29,39,49,59,69,79,89,99]
		TorF = 0
		for c in range (20):
			if i == arrN6[c]:
				TorF = 1
		if i < 11 or i > 89 or TorF == 1:
			nothing = 0
		else:
			count = standartF(1,1,1,1,1,1,1,1)
			field[i] = str(count)
		if i == 0:
			count = standartF(0,0,0,0,1,1,1,0)
			field[i] = str(count)
		if i == 9:
			count = standartF(1,0,0,0,0,0,1,1)
			field[i] = str(count)
		if i == 99:
			count = standartF(1,1,1,0,0,0,0,0)
			field[i] = str(count)
		if i == 90:
			count = standartF(0,0,1,1,1,0,0,0)
			field[i] = str(count)
		arrN2 = [10,20,30,40,50,60,70,80]
		for c in range (8):
			if i == arrN2[c]:
				count = standartF(0,0,1,1,1,1,1,0)
				field[i] = str(count)
		arrN3 = [19,29,39,49,59,69,79,89]
		for c in range (8):
			if i == arrN3[c]:
				count = standartF(1,1,1,0,0,0,1,1)
				field[i] = str(count)
		arrN4 = [1,2,3,4,5,6,7,8]
		for c in range (8):
			if i == arrN4[c]:
				count = standartF(1,0,0,0,1,1,1,1)
				field[i] = str(count)
		arrN5 = [91,92,93,94,95,96,97,98]
		for c in range (8):
			if i == arrN5[c]:
				count = standartF(1,1,1,1,1,0,0,0)
				field[i] = str(count)
print (" ")
print (" ")
for i in range (100):
	if field[i] == str(0):
		field[i] = (" ")
prin()

