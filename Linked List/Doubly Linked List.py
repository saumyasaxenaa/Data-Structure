class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.prev = None

    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length = 1
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.length += 1

    def insert(self, index, value):
        newNode = Node(value)
        if index >= self.length:
            return self.append(value)
        leader = self.traverseToIndex(index-1)
        follower = leader.next
        leader.next = newNode
        newNode.prev = leader
        newNode.next = follower
        follower.prev = newNode
        self.length += 1

    def traverseToIndex(self, index):
        counter = 0
        tempNode = self.head
        while counter != index:
            tempNode = tempNode.next
            counter += 1
        return tempNode

    def remove(self, index):
        leader = self.traverseToIndex(index-1)
        unwanted = leader.next
        follower = unwanted.next
        leader.next = follower
        follower.prev = leader
        self.length -= 1


    def printList(self):
        currNode = self.head
        while currNode != None:
            print(currNode.data, end=' <--> ')
            currNode = currNode.next



dll = DoublyLinkedList()
dll.append(10)
dll.append(5)
dll.append(16)
dll.prepend(1)
dll.insert(2,99)
dll.remove(2)
print(dll.printList())

