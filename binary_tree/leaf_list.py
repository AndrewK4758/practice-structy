class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def leaf_list(root):
  if root == None:
    return []
  leaves = []
  find_leaves(root, leaves)
  return leaves
def find_leaves(root, leaves):
  if root == None:
    return
  
  if root.left == None and root.right == None:
    leaves.append(root.val)
  find_leaves(root.left, leaves)
  find_leaves(root.right, leaves)

  
  # if root == None:
    # return []
  # leaves = []
  # stack = [root]
  # while stack:
    # cur = stack.pop()
    # if cur.right == None and cur.left == None:
      # leaves.append(cur.val)
# 
    # if cur.right != None:
      # stack.append(cur.right)
    # if cur.left != None:
      # stack.append(cur.left)
  # return leaves
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

print(leaf_list(a)) # -> [ 'd', 'e', 'f' ] 