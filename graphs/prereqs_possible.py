def prereqs_possible(num_courses, graph):
	visited = set()
	graph = adj_lst(num_courses, graph)
	print(graph)
	for node in graph:
		if dfs(graph, node, visited, temp=set()) == True:
			return False
	return True
		
def dfs(graph, cur, visited, temp):
	print(temp, 'temp', visited, 'visit')
	if cur in temp:
		return True
	if cur in visited:
		return False
	
	temp.add(cur)
		
	for neighbor in graph[cur]:
		if dfs(graph, neighbor, visited, temp):
			return True

	temp.remove(cur)
	visited.add(cur)
	return False

def adj_lst(num_courses, graph):
	adj_lst = {}
	for i in range(num_courses):
		adj_lst[i] = []
	for node in graph:
		a, b = node
		adj_lst[a].append(b)
	return adj_lst

numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
  (3, 0),
]
print(prereqs_possible(numCourses, prereqs))

'''

		0
   / \
  .   .
 1     2
  \   /
   . .
    3     4--.5


'''