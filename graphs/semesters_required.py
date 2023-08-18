def semesters_required(num_courses, prereques):
  dist = {}
  graph = adjacency(num_courses, prereqs)
  for i in range(num_courses):
     if len(graph[i]) == 0:
         dist[i] = 1
  for node in graph:
          dfs_longest_path(graph, node, dist)
  return max(dist.values())
def adjacency(num_courses, edges):
  graph = {}
  for i in range(num_courses):
    graph[i] = []
  for edge in edges:
    a, b = edge[0], edge[1]
    graph[a].append(b)
  return graph

def dfs_longest_path(graph, cur, dist):
  if cur in dist:
    return dist[cur]
  max_dist = 0
  for neighbor in graph[cur]:
    cur_dist = dfs_longest_path(graph, neighbor, dist)
    if cur_dist > max_dist:
      max_dist = cur_dist
  dist[cur] = max_dist + 1
  return dist[cur]
num_courses = 7
prereqs = [
  (4, 3),
  (3, 2),
  (2, 1),
  (1, 0),
  (5, 2),
  (5, 6),
]
print(semesters_required(num_courses, prereqs))