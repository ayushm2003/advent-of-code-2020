
class Boarding:
	seats = []

	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns

	def new(self):
		for i in range(self.rows):
			n = []
			
			for j in range(self.columns):
				n.append(str(i) + "  " + str(j))
			self.seats.append(n)
			#x = 0

	def delete(self, property, direction):
		row_length = len(self.seats)
		#column_length = len(self.seats[0])
		if property == "row":
			mid = int(row_length / 2)
			if direction == "F":
				del self.seats[mid:(row_length)]
				#print(self.seats)
			elif direction == "B":
				del self.seats[0:mid]
				'''
		elif property == "column":
			mid = int(column_length / 2)
			if direction == 
			'''


def main():
	plane = Boarding(128, 8)
	#plane.new()

	with open("trial_data.txt", "r") as f:
		patterns = f.readline()

		while patterns != "":
			plane.new()

			for pattern in patterns:
				if pattern == "F" or pattern == "B":
					plane.delete("row", pattern)
				else:
					plane.delete("column", pattern)

			print(plane.seats)
			plane.seats.clear()
			patterns = f.readline()

main()