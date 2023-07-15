class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s
s.next = t
# 5 -> 7 -> 10 -> 12 -> 20 -> 28
# 6 -> 8 -> 9 -> 25

def merge_lists(head_1, head_2):
    if head_1 == None and head_2 == None:
        return None
    if head_1 == None:
        return head_2
    if head_2 == None:
        return head_1

    if head_1.val < head_2.val:
        next_head_1 = head_1.next
        head_1.next = merge_lists(next_head_1, head_2)
    else:
        next_head_2 = head_2.next
        head_2.next = merge_lists(head_1, next_head_2)
    return head_1.val
    

        

            

    # dummy = Node(None)
    # value = dummy
    # cur1 = head_1
    # cur2 = head_2
# 
    # while cur1 != None and cur2 != None:
        # 
        # if cur1.val < cur2.val:
            # value.next = cur1
            # cur1 = cur1.next
        # else:
            # value.next = cur2
            # cur2 = cur2.next
        # value = value.next
    # if cur1 != None:
        # value.next = cur1
    # if cur2 != None:
        # value.next = cur2
# 
    # return dummy.next
          

print(merge_lists(a, q))