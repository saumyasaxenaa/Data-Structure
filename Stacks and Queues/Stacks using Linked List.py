class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.data

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            holdingPointer = self.top
            self.top = newNode
            self.top.next = holdingPointer
        self.length += 1


    def printStack(self):
        currNode = self.top
        while currNode:
            print(currNode.data,end='\n')
            currNode = currNode.next
        print('*****')

    def pop(self):
        if not self.top:
            return None
        if self.length == 0:
            self.bottom = None
        self.top = self.top.next
        self.length -= 1


myStack = Stack()
myStack.push('google')
myStack.push('Udemy')
myStack.push('Youtube')
myStack.printStack()
myStack.pop()
myStack.pop()
myStack.printStack()

