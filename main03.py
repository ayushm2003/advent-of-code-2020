# 3 steps Right, 1 Down
RIGHT = 3
DOWN = 1

TREE = "#"
c = 0

def check(n):
	a = 0
	while n > 31:
		n -= 31
		a += 1
	
	return a

with open("trial_data.txt", "r") as f:

	#read = f.readlines()
	#print(read)
	t = 4
	l = 31

	r = f.readline()
	print(len(r))
	print(f.tell())
	#print(r)
	while r != "":
		if t > 32:
			print("##########################")
			print(len(r))
			print(t)
			n = check(len(r))
			i = r * (n+1)
			print(r)
			print(t)
			d = i[:t]
			print(d)
			print("##########################")
		else:
			d = f.readline(t)
			d = str(d)
		
		if len(d) > 0 and d[len(d) - 1] == TREE:
			c += 1
		print(d)
		t += RIGHT

		r = f.readline()
		print(f.tell())

print(c)
