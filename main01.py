from itertools import product

file = open("data01.txt", "r").read().split("\n")
f = list(file)
seen = set()  # set of seen pairs

##### PART 1 ######

for (x, y) in product(f, f):
	if (x, y) not in seen and (y, x) not in seen and int(x) + int(y) == 2020:
		print(x + "   " + y)
		print(int(x) * int(y))
	if len(f) > 0:
		f.pop(0)
	seen.add((x, y))


#### PART 2 ####
# does not check for seen pairs for now

for (x, y, z) in product(f, f, f):
	if (x, y, z) not in seen and int(x) + int(y) + int(z) == 2020:
		print(x + "   " + y + "   " + z)
		print(int(x) * int(y) * int(z))
	if len(f) > 0:
		f.pop(0)