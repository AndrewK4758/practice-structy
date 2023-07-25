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

def all_tree_paths(root):
  if root == None:
    return []
  if root.left == None and root.right == None:
    return [[root.val]]
  paths = []
  left = all_tree_paths(root.left)
  for node in left:
    paths.append([root.val, *node])
  right = all_tree_paths(root.right)
  for node in right:
    paths.append([root.val, *node])
    
  return paths

  
print(all_tree_paths(a))