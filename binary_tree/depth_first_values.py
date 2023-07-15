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


def depth_first_values(root):
  if root == None:
    return []
  left_val = depth_first_values(root.left)
  right_val = depth_first_values(root.right)
  return [ root.val, *left_val, *right_val]

#   stack = [root]
#   res = []
#   if root == None:
    # return res
#   while stack:
    # cur = stack.pop()
    # print(cur.val)
    # res.append(cur.val)
    # if cur.right != None:
    #   stack.append(cur.right)
    # if cur.left != None:
    #   stack.append(cur.left)
#   return res
print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'c', 'f'])