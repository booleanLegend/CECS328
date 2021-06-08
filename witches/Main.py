"""
Name: Matthew Zaldana
Matrix Assignment 5 - Witches
Due Date: May 3, 2021
"""


def getInput():
	"""
	Gets the input of the text file and calls the matrix solver to pass the solved list to the output file
	:return: None
	"""
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
		if columns == 50:
			for column in range(columns):
				other_row = []
				for row in range(rows - 1):
					other_row.append(components[row + 1][column])
				new_row.append(other_row)
			for i in range(columns):
				new_row[i].append(components[0][i])
			output(omnipotent(new_row))
		# count += 1
		else:
			for x in range(columns):
				for i in range(1, columns + 1):
					matrix[count][i-1] = components[i][count]
				count += 1
			count = 0
			for i in range(columns):
				matrix[i][columns] = components[0][i]
				count += 1
			output(omnipotent(matrix))


def omnipotent(matrix):
	"""
	Solves the matrix by calling the other functions
	:param matrix:
	:return:
	"""
	if len(matrix) == 50:
		n = min(len(matrix), len(matrix[0])) - 1
	else:
		n = len(matrix)
	for i in range(0, n):
		maxColumn = searchMaxInColumn(i, n, matrix)
		swapMaxColumn(i, n, matrix, maxColumn)
		reduceRowForm(i, n, matrix)
	return solveMatrix(n, matrix)


def searchMaxInColumn(i, n, matrix):
	"""
	Find the max number in a column to swap that column
	:param i: iteration of column
	:param n: number of columns
	:param matrix: matrix values
	:return: index of the max column
	"""
	maxEl = abs(matrix[i][i])
	maxColumn = i
	for k in range(i + 1, n):
		if abs(matrix[k][i]) > maxEl:
			maxEl = abs(matrix[k][i])
			maxColumn = k
	return maxColumn


def swapMaxColumn(i, n, matrix, maxColumn):
	"""
	Swaps the max row with the first row to make it the pivot
	:param i: index of column
	:param n: number of columns
	:param matrix: matrix values
	:param maxColumn: index of max column
	:return: None
	"""
	for k in range(i, n + 1):
		tmp = matrix[maxColumn][k]
		matrix[maxColumn][k] = matrix[i][k]
		matrix[i][k] = tmp


def reduceRowForm(i, n, matrix):
	"""
	Makes all the rows starting at index 0 to make it reduce row echelon form
	:param i: index to start at
	:param n: number of columns
	:param matrix: matrix values
	:return: None
	"""
	for k in range(i + 1, n):
		c = -matrix[k][i] / matrix[i][i]
		for j in range(i, n + 1):
			if i == j:
				matrix[k][j] = 0
			else:
				matrix[k][j] += c * matrix[i][j]


def solveMatrix(n, matrix):
	"""
	Solves the augmented matrix
	:param n: number of columns
	:param matrix: matrix values
	:return: List of the matrix answer values
	"""
	x = [0 for _ in range(n)]
	for i in range(n - 1, -1, -1):
		x[i] = matrix[i][n] / matrix[i][i]
		for k in range(i - 1, -1, -1):
			matrix[k][n] -= matrix[k][i] * x[i]
	return x


def output(answer):
	"""
	Writes to the file
	:param answer: List of values
	:return: None
	"""
	out_file = open("output.txt", "w")
	for num in answer:
		out_file.write(str(round(num)))
		out_file.write('\n')
	out_file.close()


if __name__ == "__main__":
	getInput()
