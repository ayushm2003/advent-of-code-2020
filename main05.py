def new(rows, columns):
	seats = []
	for i in range(rows):
		n = []
		for j in range(columns):
			n.append(j)
		seats.append(n)
	
	return seats


for seat in new(5, 3):
	print(seat)
