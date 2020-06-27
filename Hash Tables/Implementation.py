from random import randint

class HashTable():
    def __init__(self):
        self.mydict = ['None']*50
        self.addr_list = []

    def __str__(self):
        return str(self.__dict__)

    def __hash(self):
        while True:
            x = randint(0,49)
            if x not in self.addr_list:
                return x

    def set(self, key, value):
        address = self.__hash()
        self.mydict[address] = [key, value]
        self.addr_list.append(address)

    def get(self, key):
        for i in self.addr_list:
            if self.mydict[i][0] == key:
                return self.mydict[i][1]

    def keys(self):
        key_arr = []
        for i in self.addr_list:
            key_arr.append(self.mydict[i][0])
        return key_arr

h = HashTable()
h.set('grapes',10)
h.set('oranges',1)
h.set('apples',2)
h.set('bananas',300)
x=h.get('grapes')
key_arr=h.keys()
print(h)
print(x)
print(key_arr)