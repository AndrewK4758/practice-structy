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

def level_averages(root):
  # recursive
  avgs = []
  levels = []
  build_levels(root, levels, 0)
  for level in levels:
    avgs.append(sum(level)/len(level))
  return avgs

def build_levels(root, levels, num):
  if root == None:
    return 
  
  if len(levels) == num:
    levels.append([root.val])
  else:
    levels[num].append(root.val)
  
  build_levels(root.left, levels, num+1)
  build_levels(root.right, levels, num+1)

  # iterative bfs
  # if root == None:
    # return []
  # avgs = []
  # levels_sums = []
  # queue = [ (root, 0)]
  # while queue:
    # cur, level = queue.pop(0)
# 
    # if len(levels_sums) == level:
      # levels_sums.append([cur.val])
      # print(levels_sums)
    # else:
      # levels_sums[level].append(cur.val)
    # print(levels_sums)
    # if cur.left != None:
      # queue.append((cur.left, level + 1))
    # if cur.right != None:
      # queue.append((cur.right, level + 1))
  # for level in levels_sums:
    # avgs.append(sum(level)/len(level))
  # return avgs
print(level_averages(a))