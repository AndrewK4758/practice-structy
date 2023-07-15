class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

def sum_list(head):
    if head == None:
        return 0
    else:
        return head.val + sum_list(head.next)
      




    # total = 0
    # current = head
    # while current != None:
    #   total += current.val
    #   current = current.next
    # return total


print(sum_list(a))