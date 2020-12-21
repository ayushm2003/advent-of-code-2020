###### PART 1 ######

TREE = "#"

def check(n, length):
	# Returns the number of time the length has to be subtraced from the next position after DOWN
	a = 0
	while n > length:
		n -= length
		a += 1
	
	return a

def count_trees(RIGHT, DOWN):
	global TREE
	c = 0

	with open("data03.txt", "r") as f:

		entries = f.readlines()
		t = 1 + RIGHT
		skip = 0

		for entry in entries:
			entry = entry[:-1]  # remove "\n"

			if skip < DOWN:
				skip += 1
				continue

			length = len(entry)

			if t > length:
				#print("t = " + str(t))
				entry = entry * (check(t, len(entry[:-1])) + 1)
				#print("e -  " + entry)
			
			d = entry[:t]
			#print(d + "  " + str(len(d)))
			#print()

			if d[len(d) - 1] == TREE:
				c += 1

			t += RIGHT
			skip = 1
	
	return c

print("c =" + str(count_trees(3, 1)))

###### PART 2 ######

directions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product = 1

for direction in directions:
	t = count_trees(direction[0], direction[1])
	#print(t)
	product *= t

print(product)
