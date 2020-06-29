class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.data

    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1

    def dequeue(self):
        if not self.first:
            return None
        if self.length == 1:
            self.last = None
        else:
            self.first = self.first.next
            self.length -= 1

    def printList(self):
        currNode = self.first
        while currNode:
            print(currNode.data,end=' ')
            currNode = currNode.next
        print('')
        print(self.length)

queue = Queue()
queue.enqueue('saumya')
queue.enqueue('Niki')
queue.enqueue('Naaz')
print(queue.peek())
queue.printList()
queue.dequeue()
queue.dequeue()
queue.printList()