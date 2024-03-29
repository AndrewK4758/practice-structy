class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

def tree_min_value(root):
  queue = [root]
  min = root.val
  while queue:
    cur = queue.pop(0)
    if cur.val < min:
      min = cur.val
    if cur.left != None:
      queue.append(cur.left)
    if cur.right != None:
      queue.append(cur.right)
  return min


print(tree_min_value(a))