class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node(7)
b = Node(5)
c = Node(1)
d = Node(2)
e = Node(8)
f = Node(9)
g = Node(3)
h = Node(4)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      7a
#    /   \
#   5b    1c
#  / \     \
# 2d  8e    9f
#    /       \
#   3g        4h

def tree_value_count(root, target):
  count= 0

  if root == None:
    return 0
  if root.val == target:
    count+=1
  print(count, 'count', tree_value_count(root.left, target), 'left', tree_value_count(root.right, target), 'right', root.val, 'root')
  return count + tree_value_count(root.left, target) + tree_value_count(root.right, target)

print(tree_value_count(a,  1))