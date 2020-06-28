# 1 --> 10 --> 99 --> 5 --> 16
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def insert(self, index, value):
        newNode = Node(value)
        if index >= self.length:
            return self.append(value)
        leader = self.traverseToIndex(index-1)
        holdingPointer = leader.next
        leader.next = newNode
        newNode.next = holdingPointer
        self.length += 1

    def traverseToIndex(self, index):
        counter = 0
        tempNode = self.head
        while counter != index:
            tempNode = tempNode.next
            counter += 1
        return tempNode

    def remove(self, index):
        leader = self.traverseToIndex(index - 1)
        unwantedNode = leader.next
        leader.next = unwantedNode.next
        self.length -= 1

    def reverse(self):
        if self.length == 1:
            return self.head
        first = self.head
        self.tail = self.head
        second = first.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first
        return self.printList()

    def printList(self):
        currNode = self.head
        while currNode != None:
            print(currNode.data, end=' --> ')
            currNode = currNode.next

mylinkedlist = LinkedList()
mylinkedlist.append(10)
mylinkedlist.append(5)
mylinkedlist.append(16)
mylinkedlist.prepend(1)
mylinkedlist.insert(2,99)
mylinkedlist.remove(1)
print(mylinkedlist.printList())
print(mylinkedlist.reverse())