#       9
#     /   \
#   4     20
#  / \   /  \
# 1  6 15  170

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            currNode = self.root
            while True:
                if value < currNode.data:
                    if currNode.left == None:
                        currNode.left = newNode
                        return
                    else:
                        currNode = currNode.left
                elif value >= currNode.data:
                    if currNode.right == None:
                        currNode.right = newNode
                        return
                    else:
                        currNode = currNode.right

    def lookup(self, value):
        if self.root == None:
            return None
        currNode = self.root
        while currNode:
            if value < currNode.data:
                currNode = currNode.left
            elif value > currNode.data:
                currNode = currNode.right
            elif currNode.data == value:
                return True
        return False

    def breadthFirstSearch(self):
        currNode = self.root
        result = []
        queue = []
        queue.append(currNode)
        while queue:
            currNode = queue.pop(0)
            result.append(currNode.data)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
        return result

    def breadthFirstSearchRecursive(self, queue, result):
        if len(queue) == 0:
            return result
        currNode = queue.pop(0)
        result.append(currNode.data)
        if currNode.left:
            queue.append(currNode.left)
        if currNode.right:
            queue.append(currNode.right)
        return self.breadthFirstSearchRecursive(queue, result)

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(f'Iterative: {tree.breadthFirstSearch()}')
print(f'Recursive: {tree.breadthFirstSearchRecursive([tree.root], [])}')
