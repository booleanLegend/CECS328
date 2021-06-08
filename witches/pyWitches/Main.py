"""
Name: Matthew Zaldana
matrixssignment 5 - Witches
Due Date: May 3, 2021
"""


def getInput():
	with open("input.txt", "r") as file:
		components = []
		for line in file:
			for num in line.split():
				components.append([int(n) for n in num.split(':')])
		columns = len(components[0])
		rows = len(components)
		matrix = [[0 for _ in range(rows)] for _ in range(columns)]
		new_row = []
		count = 0
		for x in range(columns):
			for i in range(1, columns + 1):
				matrix[count][i-1] = components[i][count]
			count += 1
		"""
		for column in range(columns):
			other_row = []
			for row in range(rows-1):
				other_row.append(components[row+1][column])
			new_row.append(other_row)
			# count += 1
		"""
		count = 0
		for i in range(columns):
			matrix[i][columns] = components[0][i]
			count += 1
		output(omnipotent(matrix))


def omnipotent(matrix):
	n = len(matrix)

	for i in range(0, n):
		maxRow = searchMaxInColumn(i, n, matrix)
		swapMaxRow(i, n, matrix, maxRow)
		reduceRowForm(i, n, matrix)
	return solveMatrix(n, matrix)


def searchMaxInColumn(i, n, matrix):
	# Search for maximum in this column
	maxEl = abs(matrix[i][i])
	maxRow = i
	for k in range(i + 1, n):
		if abs(matrix[k][i]) > maxEl:
			maxEl = abs(matrix[k][i])
			maxRow = k
	return maxRow


def swapMaxRow(i, n, matrix, maxRow):
	# Swap maximum row with current row (column by column)
		for k in range(i, n + 1):
			tmp = matrix[maxRow][k]
			matrix[maxRow][k] = matrix[i][k]
			matrix[i][k] = tmp


def reduceRowForm(i, n, matrix):
	# Make all rows below this one 0 in current column
	for k in range(i + 1, n):
		c = -matrix[k][i] / matrix[i][i]
		for j in range(i, n + 1):
			if i == j:
				matrix[k][j] = 0
			else:
				matrix[k][j] += c * matrix[i][j]


def solveMatrix(n, matrix):
	# Solve equation matrix x=b for an upper triangular matrix matrix
	x = [0 for _ in range(n)]
	for i in range(n - 1, -1, -1):
		x[i] = matrix[i][n] / matrix[i][i]
		for k in range(i - 1, -1, -1):
			matrix[k][n] -= matrix[k][i] * x[i]
	return x			

def output(answer):
	out_file = open("output.txt", "w")
	for num in answer:
		out_file.write(str(round(num)))
		out_file.write('\n')
	out_file.close()


if __name__ == "__main__":
	getInput()
