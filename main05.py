class Boarding:
	seats = []
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns

	def new(self):
		
		for i in range(self.rows):
			n = []
			for j in range(self.columns):
				n.append(j)
			self.seats.append(n)



plane = Boarding(5, 3)
plane.new()
seats = plane.seats

for seat in seats:
	print(seat)