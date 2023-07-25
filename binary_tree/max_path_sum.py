class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  def __repr__(self):
    return str(self.val)

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

def max_path_sum(root):
  if root == None:
    return float('-inf')
  
  if root.left == None and root.right == None:
    return root.val

  return root.val + max(max_path_sum(root.right), max_path_sum(root.right))
print(max_path_sum(a))