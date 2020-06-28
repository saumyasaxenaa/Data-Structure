class Array:
    def __init__(self):
        self.length = 0
        self.data = []

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data.append(item)
        self.length += 1

    def pop(self):
        self.data.pop()

    def delete(self, index):
        self.data.remove(self.get(index))
        return self.data

    def printArr(self):
        return self.data


arr = Array()
arr.push('hi')
arr.push('hello')
arr.push('you')
arr.push('are')
arr.push('nice')
print(arr.printArr())
arr.delete(1)
arr.delete(2)
print(arr.printArr())
