class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z

def zipper_lists(head_1, head_2):
    if head_1 == None and head_2 == None:
        return
    
    if head_1 == None:
        return head_2
    
    if head_2 == None:
        return head_1
    
    next_head_1 = head_1.next
    next_head_2 = head_2.next
    head_1.next = head_2
    head_2.next = zipper_lists(next_head_1, next_head_2)
    return head_1

# def zipper_lists(head_1, head_2):
    # end = head_1
    # cur1 = head_1.next
    # cur2 = head_2 
    # pos = 0
    # while cur1 != None and cur2 != None: 
        # if pos % 2 == 0:
            # end.next = cur2
            # cur2 = cur2.next
        # else:
            # end.next = cur1
            # cur1 = cur1.next
        # end = end.next
        # pos += 1      
# 
    # if cur1 != None:
        # end.next = cur1
    # if cur2 != None:
        # end.next = cur2
    # return end

print(zipper_lists(a, x))
