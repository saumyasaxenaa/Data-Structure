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

    def DFSInorder(self, currNode, result):
        if currNode:
            self.DFSInorder(currNode.left, result)
            result.append(currNode.data)
            self.DFSInorder(currNode.right, result)
        return result

    def DFSPostorder(self, currNode, result):
        if currNode:
            self.DFSPostorder(currNode.left, result)
            self.DFSPostorder(currNode.right, result)
            result.append(currNode.data)
        return result


    def DFSPreorder(self, currNode, result):
        if currNode:
            result.append(currNode.data)
            self.DFSPreorder(currNode.left, result)
            self.DFSPreorder(currNode.right, result)
        return result



tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(f'Inorder: {tree.DFSInorder(tree.root, [])}')
print(f'Postorder: {tree.DFSPostorder(tree.root, [])}')
print(f'Preorder: {tree.DFSPreorder(tree.root, [])}')