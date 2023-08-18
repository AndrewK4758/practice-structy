def undirected_path(edges, node_A, node_B):
  graph = edge_to_graph(edges)
  return has_path(graph, node_A, node_B, set())

def edge_to_graph(edges):
  graph = {}
  for i in range(len(edges)):
    a = edges[i][0]
    b = edges[i][1]
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph

def has_path(graph, src, dst, visited):
# recursive
  if src == dst:
    return True
  if src in visited:
    return False
  
  visited.add(src)
      
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited) == True:
      return True
    
  return False

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]
'''
i--j
|
k--m
|
l  o--n
'''
print(undirected_path(edges, 'j', 'm')) # -> True