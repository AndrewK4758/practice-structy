def largest_component(graph):
  visited = set()
  largest = 0

  for node in graph:
    length = graph_traversal(graph, node, visited)
    if length > largest:
      largest = length
  return largest

def graph_traversal(graph, cur, visited):
  if cur in visited:
    return 0

  visited.add(cur)

  length = 1
  for neighbor in graph[cur]:
    length += graph_traversal(graph, neighbor, visited)
  return length

print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 4


'''
      5
      | \
   1--0--8

   2---3
    \ /
     4
'''