"""
	Name: Matthew Zaldana
	Assignment: Sierpinski
"""

from decimal import Decimal as D
import math


def getPoints():
	"""
		Reads input.txt
		Stores amount of triangles to create
		Stores lines as coordinates in list	of lists
	"""
	with open("input.txt") as file:
		amt = int(file.readline())
		segs = []
		for line in file.readlines():
			x1, y1, x2, y2 = line.split(' ')
			x1, y1, x2, y2 = D(x1), D(y1), D(x2), D(y2)
			segs.append([(x1, y1), (x2, y2)])
	omnipotent(amt, segs)


def omnipotent(tri_amt, line_segs):
	"""
		Driver function, takes in amt of triangles to create and line segs
		Calls functions to see if line segs intersect triangle
		Outputs 0 if false, 1 otherwise
	"""
	# saves first coordinates
	rot_lt = [(0, 0), (math.cos(math.pi / 3), math.sin(math.pi / 3)),
				(1 + math.cos(math.pi / 3), math.sin(math.pi / 3)),
				(1 + (2 * math.cos(math.pi / 3)), 0)]
	# to save final coords
	coords = []
	for i in range(2, tri_amt + 1):
		# rotates 60 counterclockwise
		for j, k in rot_lt:
			k *= -1
			a = math.cos(math.pi / 3) * j
			a = a - (math.sin(math.pi / 3) * k)
			b = math.sin(math.pi / 3) * j
			b = b + (math.cos(math.pi / 3) * k)
			# add to final coords
			coords.append((round(a, 15) + 0, round(b, 15) + 0))
		# saves last coords for offsetting next coords
		p, q = coords[-1]
		# adjusts to last coords
		for j, k in rot_lt[1:]:
			c, d = j + p, k + q
			coords.append((round(c, 15) + 0, round(d, 15) + 0))
		# saves last coords for offsetting last coords
		r, s = coords[-1]
		# rotates 300 counterclockwise and adjusts to last coords
		for j, k in rot_lt[1:]:
			k *= -1
			e = math.cos(-math.pi / 3) * j
			e = e - (math.sin(-math.pi / 3) * k)
			e = round(e, 15)
			f = math.sin(-math.pi / 3) * j
			f = f + (math.cos(-math.pi / 3) * k)
			e, f = e + r, f + s
			coords.append((round(e, 15) + 0, round(f, 15) + 0))
		rot_lt = coords
		print(rot_lt)
		coords = []
	# iterate over all line sgs against triangle coordinates to see if it intersects
	# if that line segments intersects then it breaks and writes a 1 to the output file and continues, 
	# otherwise writes a 0 and continues
	coords = rot_lt
	once_found = False
	to_Write = []
	each_coord = []
	out = open('output.txt', 'w')
	out.close()
	out = open('output.txt', 'w')
	for tuple_lines in line_segs:
		for i, tuple_coords in enumerate(coords):
			print(tuple_lines, tuple_coords)
			if 1 + i < len(coords) and i - 1 >= 0:
				if isTouching(tuple_lines, coords[i - 1], tuple_coords):
					# each_coord.append(1)
					out.write("1\n")
					once_found = True
					break
				# else:
				# 	each_coord.append(0)
			elif 1 + i == len(coords):
				if isTouching(tuple_lines, coords[i - 1], tuple_coords):
					# each_coord.append(1)
					out.write("1\n")
					once_found = True
					break
				else:
					out.write("0\n")
		# to_Write.append(each_coord)
	out.close()


def isTouching(segs, tri_pt1, tri_pt2):
	"""
		Iterates over all line segs against triangle coordinates to see one intersects
		Unpacks the segs as x,y values
		Unpacks the triangle coordinate points as x,y values and converts them to decimal
		Returns a boolean from algorithm
	"""
	lseg1, lseg2 = segs
	lx1, ly1 = lseg1  # A.x and A.y
	lx2, ly2 = lseg2  # B.x and B.y
	tptx1, tpty1 = tri_pt1  # C.x and C.y
	tptx1, tpty1 = D(tptx1), D(tpty1)
	tptx2, tpty2 = tri_pt2  # D.x and D.y
	tptx2, tpty2 = D(tptx2), D(tpty2)
	# lseg1, tri_pt1, tri_pt2 != lseg2, tri_pt1, tri_pt2 and lseg1, lseg2, tri_pt1 != lseg1, lseg2, tri_pt2
	# A, B, C
	# C.y-A.y * B.x-A.x > B.y-A.y * C.x-A.x
	# one = (((tpty2 - ly1) * (tptx1 - lx1)) > ((tpty1 - ly1) * (tptx2 - lx1)))
	# two = (((tpty2 - ly2) * (tptx1 - lx2)) > ((tpty1 - ly2) * (tptx2 - lx2)))
	# three = (((tpty1 - ly1) * (lx2 - lx1)) > ((ly2 - ly1) * (tptx1 - lx1)))
	# four = (((tpty2 - ly1) * (lx2 - lx1)) > ((ly2 - ly1) * (tptx2 - lx1)))
	# is_intersecting = (one != two) and (three != four)
	is_intersecting = (((((tpty2 - ly1) * (tptx1 - lx1)) > ((tpty1 - ly1) * (tptx2 - lx1))) != (
			((tpty2 - ly2) * (tptx1 - lx2)) > ((tpty1 - ly2) * (tptx2 - lx2))))
			and
			((((tpty1 - ly1) * (lx2 - lx1)) > ((ly2 - ly1) * (tptx1 - lx1))) != (
				((tpty2 - ly1) * (lx2 - lx1)) > ((ly2 - ly1) * (tptx2 - lx1)))))
	return is_intersecting


def true_intersection():
	"""
		Returns True if given 4 points they intersect
	"""
	print()
	return True


if __name__ == "__main__":
	getPoints()
