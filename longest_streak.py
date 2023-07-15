class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node(9)
b = Node(9)
c = Node(1)
d = Node(9)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

def longest_streak(head, pre_val = None):
   cur_cnt = 1
   lng_cnt = 0
   cur = head
   pre_val = None  
   while cur != None:
       if pre_val == cur.val:
          cur_cnt+=1
       else:
          cur_cnt = 1
       pre_val = cur.val
       cur = cur.next
       if cur_cnt > lng_cnt:
          lng_cnt = cur_cnt
   return lng_cnt


print(longest_streak(a))