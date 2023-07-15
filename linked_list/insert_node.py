class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node("a")
b = Node("b")

a.next = b


def insert_node(head, value, index):
    pos = 0
    cur = head
    node_val = Node(value)
    if index == 0:
        head = Node(value)
        head.next = cur
    else:
        while cur != None:
            if pos == index - 1:
                link = cur.next
                cur.next = node_val
                node_val.next = link
            pos+=1
            cur = cur.next
    return head.val
        
print(insert_node(a, 'z', 0))