'''2. Write a Python program to set a new value of an item in a singly linked list using index value.'''

class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Createe an empty list
        self.tail = None
        self.head = None
        self.count = 0

    def append_item(self, data):
        #Append items on the list
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1
    
    def __getitem__(self, index):
        if index > self.count - 1:
            return "Index out of range"
        current_val = self.tail
        for n in range(index):
            current_val = current_val.next
        return current_val.data
    
    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.tail
        for n in range(index):
            current = current.next
        current.data = value

items = singly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')

print("Modify items by index:")
items[1] = "SQL"
print("New value: ",items[1])
items[4] = "Perl"
print("New value: ",items[4])
