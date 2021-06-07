# store the number for n * n grid
# for an n * n grid, count the amount of vertical walls and save to variable v
# count v lines in input and save numbers in list
# get rest of lines and save horizontal wall values in list
"""
Name: Matthew Zaldana
Assignment: Maze
"""

from decimal import Decimal as D


def get_input():
	all_lines = []
	with open("input.txt") as file:
		grid_n_size = int(file.readline())
		for line in file.readlines():
			all_lines.append(D(line))
	vertical_lines, horizontal_lines = all_lines[:len(all_lines) // 2], all_lines[len(all_lines) // 2:]
	omnipotent(grid_n_size, vertical_lines, horizontal_lines)


def omnipotent(grid_size: int, v_lines: list, h_lines: list):
	max_v_lines = []
	max_h_lines = []
	count = 0
	for i in range(grid_size):
		max_temp = v_lines[count]
		dump_max = []
		for j in range(1, len(v_lines) - 1):
			if v_lines[j] > max_temp:
				max_v_lines.append(v_lines[j])
			else:
				dump_max.append(max_temp)
				max_temp = v_lines[j]
				if max_temp not in max_v_lines:
					max_v_lines.append(max_temp)
		count += grid_size - 1

	print()


if __name__ == "__main__":
	get_input()
