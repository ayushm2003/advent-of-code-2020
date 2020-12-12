from operator import xor

file = open("data02.txt", "r").read().split("\n")
entries = list(file)

c = 0

for entry in entries:
	parts = entry.split()
	
	n = parts[0].split("-")
	lower = int(n[0])
	higher = int(n[1])
	character = parts[1][0]
	string = parts[2]

	####### PART 1 ########

	'''
	k = 0

	for char in string:
		if char == character:
			k += 1
	
	if k >= lower and k <= higher:
		c += 1
	'''

	####### PART 2 #######
	flag1 = False
	flag2 = False

	if string[lower-1] == character: flag1 = True
	if string[higher-1] == character: flag2 = True

	if xor(flag1, flag2):
		c += 1

print(c)