# 3 steps Right, 1 Down
'''
RIGHT = 3
DOWN = 1
'''
TREE = "#"
#c = 0

def check(n, length):
	a = 0
	while n > length:
		n -= length
		a += 1
	
	return a

def trees(RIGHT, DOWN):
	c = 0
	with open("trial_data.txt", "r") as f:

		entries = f.readlines()
		line = 0
		t = 1 + RIGHT
		skip = 0

		for entry in entries:
			line += 1

			if skip < DOWN:
				skip += 1
				continue

			length = len(entry)

			if t > len(entry):
				#print("t = " + str(t))
				entry = entry[:-1] * (check(t, len(entry[:-1])) + 1)
				#print(entry)
			
			d = entry[:t]
			#print(d)
			if d[len(d) - 1] == TREE:
				c += 1

			t += RIGHT
			skip = 1
	
	return c

print("c =" + str(trees(7, 1)))