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
                    currNode = currNode.left
                elif value >= currNode.value:
                    if currNode.right == None:
                        currNode.right = newNode
                        return
                    currNode = currNode.right

    def lookup(self, value):
        if self.root == None:
            return None
        currNode = self.root
        while currNode:
            if value < currNode.value:
                currNode = currNode.left
            elif value > currNode.value:
                currNode = currNode.right
            elif currNode.value == value:
                return True
        return False

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
print(tree.printTree())