def longest_path(graph):
    dist = {}
    
    for node in graph:
        if graph[node] == []:
            dist[node] = 0

    for node in graph:
        dfs_dist(graph, node, dist)
    return max(dist.values())

def dfs_dist(graph, cur, dist):
    if cur in dist:
        return dist[cur]
    
    max_dist = 0
    for neighbor in graph[cur]:
        cur_dist = dfs_dist(graph, neighbor, dist)
        if cur_dist > max_dist:
            max_dist = cur_dist
            
    dist[cur] = max_dist + 1
    return dist[cur]

graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

print(longest_path(graph)) # -> 2