def has_path(graph, src, dst):
# recursive
  if src == dst:
    return True
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True
    
  return False
    
  # return False
  
  # iterative
  # stack = [src]
  # while stack:
    # cur = stack[-1]
    # print(cur, stack)
    # stack.pop()
    # for vert in graph[cur]:
      # stack.append(vert)
    # if cur == dst:
      # return True
  # return False 

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'k'))

'''
      f--i--k
      |/ |
      g  j
      |
      h
'''