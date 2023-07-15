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

def reverse_list(head, previous=None):
    if head == None:
        return previous
    next = head.next
    head.next = previous
    return reverse_list(next, head)






    # previous = None
    # current = head
    # while current != None:
        # next = current.next
        # current.next = previous
        # previous = current
        # current = next
    # return previous.val
reverse = reverse_list(a)

while reverse != None:
    print(reverse.val)