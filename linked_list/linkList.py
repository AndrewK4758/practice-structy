class listNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class linkedList:
    def __init__(self):
        self.head = listNode()
    
    def append(self, val):
        new_node = listNode(val)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.val)
        print(elems)

myList = linkedList()



myList.append('a')
myList.append('b')
myList.append('c')
myList.append('d')
myList.append('e')
myList.append('f')


myList.display()