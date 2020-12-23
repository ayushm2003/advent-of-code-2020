
class Boarding:
	seats = []
	highest_ID = 0

	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns

	def new(self):
		for i in range(self.rows):
			n = []
			
			for j in range(self.columns):
				n.append(str(i) + "  " + str(j))
			self.seats.append(n)

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
		
	def seat_ID(self):
		position = self.seats[0][0].split()
		ID = (int(position[0]) * 8) + int(position[1])
		if ID > self.highest_ID:
			self.highest_ID = ID
		


def main():
	plane = Boarding(128, 8)

	with open("data05.txt", "r") as f:
		patterns = f.readline()

		while patterns != "":
			plane.new()

			for pattern in patterns:
				plane.delete(pattern)

			plane.seat_ID()

			plane.seats.clear()
			patterns = f.readline()

	print(plane.highest_ID)

main()