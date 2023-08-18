def has_cycle(graph):
		visited = set()
		for node in graph:
				if dfs(graph, node, visited, temp=set()):
						return True
		return False

def dfs(graph, cur, visited, temp):
		print(temp, 'temp', visited, 'visited')
		if cur in visited:
				return False
		if cur in temp:
				return True
		
		temp.add(cur)
		for neighbor in graph[cur]:
				if dfs(graph, neighbor, visited, temp):
						return True
		
		temp.remove(cur)
		visited.add(cur)
		return False

print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["d"],
  "d": ["b"],
}))
	

'''

		a
   / \
  .   .
 b-----c
			  \
				 .
					d
'''