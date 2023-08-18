def connected_components_count(graph):
  visited = set()
  count = 0

  for node in graph:
    if traverse_graph(graph, node, visited) == True:
      count+=1
  return count
  
def traverse_graph(graph, cur, visited):
  if cur in visited:
    return False
  
  visited.add(cur)

  for neighbor in graph[cur]:
    traverse_graph(graph, neighbor, visited)
  return True

print(connected_components_count({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
})) # -> 5


'''  
     7  3
     |
  4--6--5
     |
     8

     1--2
'''