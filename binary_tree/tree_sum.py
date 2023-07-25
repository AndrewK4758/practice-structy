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

def tree_sum(root):
  stack = [root]
  res = 0
  if root == None:
    return res
  while stack:
    cur = stack.pop()
    res += cur.val
    if cur.right != None:
      stack.append(cur.right)
    if cur.left != None:
      stack.append(cur.left)
  return res

#   if root == None:
    # return 0
#   left_val = tree_sum(root.left)
#   right_val = tree_sum(root.right)
#   return root.val + left_val + right_val


print((tree_sum(a)))