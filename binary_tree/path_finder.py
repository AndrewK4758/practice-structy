class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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
def path_finder(root, target):
  result = _path_finder(root, target)
  if result == None:
    return None
  else:
    return result[::-1]

def _path_finder(root, target):
  if root == None:
    return None
  
  if root.val == target:
    return [root.val]
  
  left_val = _path_finder(root.left, target)
  if left_val != None:
    left_val.append(root.val)
    return left_val  
  right_val = _path_finder(root.right, target)
  if right_val != None:
    right_val.append(root.val)
    return right_val

  return None
print(path_finder(a, 'e'))

