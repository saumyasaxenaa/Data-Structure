#       9
#     /   \
#   4     20
#  / \   /  \
# 1  6 15  170

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            currNode = self.root
            while True:
                if value < currNode.value:
                    if currNode.left == None:
                        currNode.left = newNode
                        return
                    else:
                        currNode = currNode.left
                elif value >= currNode.value:
                    if currNode.right == None:
                        currNode.right = newNode
                        return
                    else:
                        currNode = currNode.right

    def lookup(self, value):
        currNode = self.root
        while True:
            if currNode == None:
                return False
            if currNode.value == value:
                return True
            elif value < currNode.value:
                currNode = currNode.left
            else:
                currNode = currNode.right

    def printTree(self):
        if self.root:
            self.Inorder(self.root)

    def Inorder(self, currNode):
        if currNode:
            self.Inorder(currNode.left)
            print(str(currNode.value))
            self.Inorder(currNode.right)


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.printTree()
print(tree.lookup(1))