from collections import deque
import pprint
def shortest_path(edges, node_A, node_B):
    graph = adj_list(edges)
    return find_path(graph, node_A, node_B)

def adj_list(edges):
    graph = {}

    for edge in edges:
        a, b = edge[0], edge[1]
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    pprint.pprint(graph)
    return graph

def find_path(graph, node_A, node_B):
    visited = set([node_A])
    queue = deque([(node_A, 0)])

    while queue:    
        node, count = queue.popleft()
        if node == node_B:
            return count
        for neighbor in graph[node]:
               if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, count + 1))
    return -1
edges = [  
  ['w', 'x'],
  ['x', 'y'],
  ['b', 'y'],
  ['z', 'v'],
  ['w', 'v'],
  ['v', 'a'],
  ['a', 's'],
  ['s', 't'],
  ['t', 'y'],
  ['y', 'd'],
  ['d', 'f'],
  ['f', 'j']
]

print(shortest_path(edges, 'x', 'j')) # -> 2

''' y--z 
    |   \
    x--w--v

'''