class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None

    def addAtEnd(self, val):
        if not self.head:
            self.head = self.tail = Node(val)
            return
        self.tail.next = Node(val, prev=self.tail)
        self.tail = self.tail.next

    def delete(self, node):
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end='->')
            temp = temp.next
        print('None')


dll = DoublyLinkedList()
for val in [1, 2, 3, 4, 5]:
    dll.addAtEnd(val)
dll.display()
dll.delete(dll.head.next.next.next.next)
dll.display()
dll.delete(dll.head)
dll.display()
