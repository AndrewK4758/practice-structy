class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a1 = Node(9)
a2 = Node(8)
a1.next = a2
# 9 -> 8

b1 = Node(7)
b2 = Node(4)
b1.next = b2
# 7 -> 4

def add_lists(head_1, head_2, carry = 0):
  if head_1 == None and head_2 == None and carry == 0:
    return None
  val1 = head_1.val if head_1 != None else 0
  val2 = head_2.val if head_2 != None else 0
  
  sum = val1 + val2 + carry
  carry = 1 if sum > 9 else 0
  num = sum % 10

  res = Node(num)

  next1 = head_1.next if head_1 != None else None
  next2 = head_2.next if head_2 != None else None

  res.next = add_lists(next1, next2, carry)
  return res





#   cur1 = head_1
#   cur2 = head_2
#   dummy_head = Node(None)
#   tail = dummy_head
#   carry = 0
#   
#   while cur1 != None or cur2 != None or carry == 1:
    # val1 = 0 
    # val2 = 0
    # if cur1 != None:
    #   val1 = cur1.val
    # if cur2 != None:
    #   val2 = cur2.val
    #   
    # sum = val1 + val2 + carry  
    # carry = 1 if sum > 9 else 0
    # num = sum % 10
    # tail.next = Node(num)
    # tail = tail.next
# 
    # if cur1 != None:
    #   cur1 = cur1.next
    # if cur2 != None:
    #   cur2 = cur2.next
# 
#   return dummy_head.next.val

print(add_lists(a1, b1))