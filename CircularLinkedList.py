# Circular Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, newData):
        self.data = newData
    
    def set_next(self, nextNode):
        self.next = nextNode

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get_head(self):
        return self.head

    def addBegin(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            return
        
        newNode.set_next(self.head)
        self.head = newNode
        self.tail.set_next(self.head)
    
    def addEnd(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            return
        
        self.tail.set_next(newNode)
        self.tail = newNode
        self.tail.set_next(self.head)

    def addBetween(self, data, data_before):
        newNode = Node(data)
        curr = self.head
        while curr.get_next().get_data() != data_before:
            curr = curr.get_next()
        node_after = curr.get_next()
        curr.set_next(newNode)
        newNode.set_next(node_after)
    
    def display(self):
        curr = self.head
        while True:
            print(curr.get_data())
            curr = curr.get_next()
            if curr == self.head:
                break
    
    def find(self,data):
        curr = self.head
        while True:
            if curr.get_data() == data:
                return curr
            curr = curr.get_next()
            if curr == self.head:
                return None

    def get_size(self):
        pass

cll = CircularLinkedList()
cll.addEnd(1)
cll.addEnd(2)
cll.addEnd(3)
cll.addEnd(4)
cll.display()
# node_4 = cll.find(4)
# after_4 = node_4.get_next().get_data()
# print("After 4:",after_4)