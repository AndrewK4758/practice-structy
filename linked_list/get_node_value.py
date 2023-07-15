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



def get_node_value(head, index):
    if index == 0:
        return head.val
    elif head == None:
        return None
    else:
      index-=1
    return get_node_value(head.next, index)




    # current = head
    # count = 0
    # while current != None:
      # if count == index:
          # return current.val
      # else:
        # count+=1
        # current = current.next
print(get_node_value(a, 2))
