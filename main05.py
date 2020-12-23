
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

	def delete(self, direction):
		row_length = len(self.seats)
		column_length = len(self.seats[0])
		mid_row = int(row_length / 2)
		mid_column = int(column_length / 2)

		if direction == "F":
			del self.seats[mid_row:row_length]
		elif direction == "B":
			del self.seats[0:mid_row]
		elif direction == "L":
			del self.seats[0][mid_column:column_length]
		elif direction == "R":
			del self.seats[0][0:mid_column]
		


def main():
	plane = Boarding(128, 8)

	with open("trial_data.txt", "r") as f:
		patterns = f.readline()

		while patterns != "":
			plane.new()

			for pattern in patterns:
				plane.delete(pattern)

			print(plane.seats)
			plane.seats.clear()
			patterns = f.readline()

main()