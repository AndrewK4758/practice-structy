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

def breadth_first_values(root):
  queue = [ root ]
  res = []

  if root == None:
    return res
  while queue:
    cur = queue.pop(0)
    res.append(cur.val)
    if cur.left != None:
      queue.append(cur.left)
    if cur.right != None:
      queue.append(cur.right)

  return res

print(breadth_first_values(a))