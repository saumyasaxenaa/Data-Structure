class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        lastitem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return lastitem

    def delete(self, index):
        deleteditem = self.data[index]
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1] # shifting the items to the left by one
        del self.data[self.length-1]
        self.length -= 1
        return deleteditem



arr = Array()
arr.push('hi')
arr.push('hello')
arr.push('you')
arr.push('are')
arr.push('nice')
print(arr)
arr.delete(1)
print(arr)
arr.delete(2)
print(arr)
