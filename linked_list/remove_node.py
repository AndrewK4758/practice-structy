class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

def remove_node(head, target_val, pre_val = None):
  
    if head.val == None:
        return None
    if head.val == target_val:
        return head.next
    
    head.next = remove_node(head.next, target_val)
    return head.val
  
  
    # if head.val == target_val:
        # return head.next
    # cur = head
    # pre_val = None
    # while cur != None:
        # if cur.val == target_val:
            # pre_val.next = cur.next
            # break
        # pre_val = cur
        # cur = cur.next
    # return head

print(remove_node(a, 'c'))