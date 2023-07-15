class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node(7)
b = Node(7)
c = Node(7)

a.next = b
b.next = c

def is_univalue_list(head, pre_val = None):
    if head == None:
       return True
    if pre_val != None and head.val != pre_val:
       return False
    return is_univalue_list(head.next, head.val)









    # cur = head
    # while cur != None:
        # if head.val == cur.val:
            # cur = cur.next
        # else:
            # return False
    # return True
        
    


print(is_univalue_list(a))

