class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node(42)

#       3
#    /    \
#   11     10
#  / \      \
# 4   -2     1

def bottom_right_value(root):
  queue = [root]
  while queue:
    cur = queue.pop(0)
    if cur.left != None:
      queue.append(cur.left)
    if cur.right != None:
      queue.append(cur.right)
  else:
    return cur.val
print(bottom_right_value(a))