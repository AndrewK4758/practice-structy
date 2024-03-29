class Node:
  def __init__(self,val):
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

def how_high(node):
  if node == None:
    return -1

  return max(how_high(node.left), how_high(node.right)) + 1


print(how_high(a))