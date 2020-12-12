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

	k = 0

	for char in string:
		if char == character:
			k += 1
	
	if k >= lower and k <= higher:
		c += 1


print(c)