from collections import deque
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

def tree_levels(root):


  
  
  
  #BFS Iteration
    '''
  if root == None:
    return []
  queue = [ (root, 0) ]
  levels = []
  while queue:
    cur, level = queue.pop(0)
    if len(levels) == level:
      levels.append([cur.val])
    else:
      levels[level].append(cur.val)
    if cur.left != None:
      queue.append((cur.left, level + 1))

    if cur.right != None:
      queue.append((cur.right, level + 1))
  return levels
  '''
print(tree_levels(a))

