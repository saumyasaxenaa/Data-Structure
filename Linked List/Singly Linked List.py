class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_Empty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert_at_head(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        return self.head

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.get_head() is None:
            self.head = new_node
            return
        temp = self.get_head()

        while temp.next:
            temp = temp.next
        temp.next = new_node
        return

    def search(self, value):
        temp = self.get_head()
        while temp:
            if temp.data == value:
                print('Element found')
                return True
            temp = temp.next
        return False

    def delete_at_head(self):
        first = self.get_head()
        if first is not None:
            self.head = first.next
            first.next = None
        return

    def delete_val(self, value):
        deleted = False
        if self.is_Empty():
            print('List is Empty')
            return deleted
        first = self.get_head()
        prev = None
        if first.data is value:
            self.delete_at_head()
            deleted = True
            return deleted
        while first is not None:
            if value is first.data:
                prev.next = first.next
                first.next = None
                deleted = True
                break
            prev = first
            first = first.next
        return deleted


lst = LinkedList()
print(lst.get_head())
for i in range(1, 10):
    lst.insert_at_head(i)
print(lst.get_head())
lst.insert_at_tail(100)
print(lst.search(100))
lst.delete_at_head()
lst.delete_val(9)
print(lst.search(9))

