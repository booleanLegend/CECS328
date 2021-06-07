""" 'Graph' Class
Simple graph class taken from CECS 274 - Data Structures - Dr. Oscar Morales Ponce
Modified for use for robot delivery problem
Adds edges, vertices, and finds path between vertices
"""


class Intersection(object):
	def __init__(self, size: int, intersec=None):
		"""
		Class Constructor
		:param size: amount of intersections
		:param intersec: nodes of graphs (vertices)
		"""
		if intersec is None:
			intersec = {}
		self.intersections = intersec  # empty dict
		self.weights = [[0 for _ in range(size)] for _ in range(size)]

	def get_edge(self, vertex):
		"""
		Get edges of vertex
		:param vertex: Dict key to look up
		:return: Key(vertex)'s values
		"""
		return self.intersections[vertex]

	def all_vertices(self):
		"""
		Get all vertices of graph
		:return: Dict keys as list
		"""
		return self.intersections.keys()

	def all_edges(self):
		"""
		Get all edges of graph
		Checks all keys and values, compares as tuple to existing edges
		Adds as key, value if non-existent, skips otherwise
		:return: Edges as list
		"""
		edges = []
		for vertex in self.intersections:
			for connected_node in self.intersections[vertex]:
				if (vertex, connected_node) not in edges:
					edges.append((vertex, connected_node))
				else:
					edges.append((vertex, connected_node))
		return edges

	def add_vertex(self, vertex):
		"""
		Adds vertex as key with empty value as list if not in instance variable, ignores otherwise
		:param vertex: Key to check and add
		:return: None
		"""
		if vertex not in self.intersections:
			self.intersections[vertex] = []

	def add_edge(self, edge):
		"""
		Adds edge as value to key if key exists, otherwise, creates key and adds edge as value
		:param edge: Tuple representing to connected vertices
		:return: None
		"""
		if edge[0] in self.intersections:
			self.intersections.setdefault(edge[0], []).append(edge[1])
		else:
			self.intersections[edge[0]] = [edge[1]]

	def add_weight(self, vertex1, vertex2, weight):
		"""
		Adds a weight to edge given vertices
		:param vertex1: Vertex with out edge
		:param vertex2: Vertex with in edge
		:param weight: Cost of travel using edge between vertex1 and vertex2
		:return: None
		"""
		self.weights[vertex1][vertex2] = weight

	def get_weight(self, vertex1, vertex2):
		"""
		Gets weight of edge
		:param vertex1: Start node
		:param vertex2: End node
		:return: Weight as int
		"""
		return self.weights[vertex1][vertex2]

	def pathfinder(self, beginning_vertex, final_vertex, path=None):
		"""
		Finds path between 2 vertices
		If start vertex is not in intersections, no path exists
		If no path exists, make one with start vertex
		If start and end vertex are same, return either
		Iterate over values of start(current) vertex as key
			If value is not in path, recursive call function with current vertex as start vertex
		:param beginning_vertex: Start vertex
		:param final_vertex: End vertex
		:param path: Empty (becomes list)
		:return: Path as list if it exists, None otherwise
		"""
		if beginning_vertex not in self.intersections:
			return None
		if path == None:
			path = []
		path = path + [beginning_vertex]
		if beginning_vertex == final_vertex:
			return path
		for vertex in self.intersections[beginning_vertex]:
			if vertex not in path:
				extra = self.pathfinder(vertex, final_vertex, path)
				if extra:
					return extra
		return None

	def all_pathfinder(self, current_vertex, end_vertex, path):
		"""
		Finds all paths between two vertices
		If start vertex is not in intersections -> empty list
		If start and end vertex are same -> new path with either
		Iterate over all values of start vertex as key
			Check if value is in path, recursive call function with current value as start vertex if not
			Add path to all paths
		:param current_vertex: Current vertex to start at
		:param end_vertex: End vertex to end
		:param path: Path of vertices as list
		:return: List of path as list of lists
		"""
		path = path + [current_vertex]
		if current_vertex == end_vertex:
			return [path]
		if current_vertex not in self.intersections:
			return []
		paths = []
		for vertex in self.intersections[current_vertex]:
			if vertex not in path:
				extra = self.all_pathfinder(vertex, end_vertex, path)
				for path in extra:
					paths.append(path)
		return paths

	def __iter__(self):
		""" allows us to iterate over keys """
		self.obj = iter(self.intersections)
		return self.obj

	def __next__(self):
		""" allows us to iterate over the vertices """
		return next(self.obj)

	def __str__(self):
		""" overridden function that allows us to return vertices and edges """
		res = "vertices: "
		for k in self.intersections:
			res += str(k) + " "
		res += "\nedges: "
		for edge in self.all_edges():
			res += str(edge) + " "
		return res


def getIntersections():
	"""
	Opens the input.txt file to retrieve intersection and matrices
	Adds vertices, edges, and weights to graph
	Calls omnipotent function with needed parameters
	:return: None
	"""
	with open("input.txt") as file:
		intersections = int(file.readline())
		graph = Intersection(intersections)
		count = 0
		matrix = [[None for _ in range(intersections)] for _ in range(intersections)]
		for line in file:
			line_int = list(map(int, line.split()))
			for j in range(intersections):
				matrix[count][j] = line_int[j]
			count += 1
		for i in range(intersections):
			for j in range(intersections):
				if matrix[i][j] != 0:
					graph.add_vertex(i)
					graph.add_edge([i, j])
				graph.add_weight(i, j, matrix[i][j])
	omnipotent(intersections, matrix, graph)
	isSC(graph, intersections)
	outputCircuit(graph)


def omnipotent(num_of_intersections: int, matrix_representations: list, graph):
	"""
	:param num_of_intersections: number of intersections
	:param matrix_representations: matrix representation of intersections
	:param graph: Intersections class objects for current input.txt file
	:return: None
	"""
	out_edges = [0] * num_of_intersections
	in_edges = [0] * num_of_intersections
	for i in range(num_of_intersections):
		for j in range(num_of_intersections):
			if matrix_representations[i][j] != 0:
				out_edges[i] += 1
				in_edges[j] += 1
	add_edges = []
	for i in range(num_of_intersections):
		if out_edges[i] != in_edges[i]:
			minimum = min(out_edges[i], in_edges[i])
			dif = abs(out_edges[i] - in_edges[i])
			if minimum == out_edges[i]:
				add_edges.append((i, dif, 'o'))
			else:
				add_edges.append((i, dif, 'i'))
	min_cost_edges = {}
	# gets all paths for a pair, adds the min cost path of pair
	for edge in add_edges:
		if edge[2] == 'o':
			for i in range(edge[1]):
				for pair in makePairs(add_edges):
					all_paths_for_pair = graph.all_pathfinder(pair[0], pair[1], [])
					path, weight = lowCostPath(all_paths_for_pair, graph)
					min_cost_edges.setdefault(tuple(path), []).append(weight)
					# min_cost_edges[tuple(path)] = weight
	new_edges = []
	for key, value in bestPair(min_cost_edges).items():
		for i in range(len(value)):
			new_edges.append((key, value))
	add_new_edges(new_edges, graph)


def makePairs(pairs):
	"""
	Makes pairs between vertices that need out edges to others needing in edges
	:param pairs: Edges that don't have enough in or out edges
	:return: List of possible pairs of edges
	"""
	edge_pairs = []
	for edge in pairs:
		if edge[2] == 'o':
			for neighbor in pairs:
				if neighbor[2] == 'i':
					edge_pairs.append((edge[0], neighbor[0]))
	return edge_pairs


def lowCostPath(paths, graph):
	"""
	Returns the pair of a path with the lowest cost to add to the graph by comparing weights of one path to another
	:param paths: paths from vertex v to u1, u2, ... u_n
	:param graph: graph with vertices and edges to get weights of edge
	:return: a tuple with the lowest path and its weight
	"""
	weights = [0 for _ in range(len(paths))]
	count = 0
	for path in paths:
		for index, item in enumerate(path):
			if index < len(path) - 1:
				weights[count] += graph.get_weight(item, path[index + 1])
		count += 1
	return paths[weights.index(min(weights))], min(weights)


def bestPair(all_pairs):
	"""
	Finds the pair with the lowest weight of edges to add by removing them if the next one has lower cost
	:param all_pairs: Pairs of edges to add
	:return: Dictionary with pairs and weights to add to graph
	"""
	weights = {}
	first_key, MAX_WEIGHT = all_pairs.popitem()
	weights[first_key] = MAX_WEIGHT
	if len(all_pairs) == 0:
		return weights
	for pair in all_pairs.values():
		for other_pair in all_pairs.values():
			if pair != other_pair:
				if pair[1] + other_pair[1] < MAX_WEIGHT:
					all_pairs.popitem()
					weights.popitem()
					weights[(tuple(pair), tuple(other_pair))], MAX_WEIGHT = pair + other_pair
	return weights


def add_new_edges(edges, graph):
	"""
	Adds the new lowest cost edges to graph with edge and vertex
	:param edges: Edges to add
	:param graph: Graph of intersections
	:return: None
	"""
	for key, value in edges:
		for i in range(len(key)-1):
			graph.add_edge([key[i], key[i+1]])
			graph.add_weight(key[i], key[i+1], value)


def isSC(graph, n):
	"""
	Checks each vertex to see if it has at least one edge, tracks all visited vertices, using deep first search, going
	backwards on each successive call
	:param graph: Intersections
	:param n: Num of intersections
	:return: List of vertices as path
	"""
	discovered = [False] * n
	for i in range(n):
		if len(graph.intersections[i]):
			dfs(graph, i, discovered)
			break
	discovered[:] = [False] * n
	m = makeDuplicate(graph, n)
	dfs(m, i, discovered)


def dfs(graph, vertex, found):
	"""
	Deep first search on graph
	:param graph: Intersections
	:param vertex: Vertex to check
	:param found: list of vertices checked
	:return: None
	"""
	found[vertex] = True
	for prev in graph.intersections[vertex]:
		if not found[prev]:
			dfs(graph, prev, found)


def makeDuplicate(graph, node_amount):
	"""
	Second dfs on graph to go backwards on edge
	:param graph:
	:param node_amount:
	:return: duplicated graph
	"""
	r = Intersection(node_amount)
	for node in range(node_amount):
		for rev_node in graph.intersections[node]:
			r.add_edge((rev_node, node))
	return r


def outputCircuit(graph):
	"""
	Prints the final eulerian path in the circuit
	Uses a stack to check all vertices
	:param graph: Final graph
	:return: None
	"""
	out = open("output.txt", "w")
	num_of_edges = {}
	for i in range(len(graph.intersections)):
		num_of_edges[i] = len(graph.intersections[i])
	current_path = []
	final_circuit = []
	current_path.append(0)
	curr_vertex = 0
	while len(current_path):
		if num_of_edges[curr_vertex]:
			current_path.append(curr_vertex)
			next_v = graph.intersections[curr_vertex][-1]
			num_of_edges[curr_vertex] -= 1
			graph.intersections[curr_vertex].pop()
			curr_vertex = next_v
		else:
			final_circuit.append(curr_vertex)
			curr_vertex = current_path[-1]
			current_path.pop()
	for i in range(len(final_circuit) - 1, -1, -1):
		out.write(str(final_circuit[i]))
		out.write(" ")


if __name__ == "__main__":
	getIntersections()
