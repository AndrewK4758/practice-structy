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

def tree_includes(root, target):
  queue = [root]
  if root == None and target != root:
    return False
  while queue:
    cur = queue.pop(0)
    if cur.val == target:
      return True
    if cur.left != None:
      queue.append(cur.left)
    if cur.right != None:
      queue.append(cur.right)
  return False

print(tree_includes(a, "a"))