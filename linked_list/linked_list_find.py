class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d


def linked_list_find(head, target):
    if head == None:
        return False
    if head.val == target:
        return True
    return linked_list_find(head.next, target)

        




    # res = False
    # current = head
    # while current != None:
        # if current.val == target:
            # res = True
        # current = current.next
    # return res

print(linked_list_find(a, 'c'))
