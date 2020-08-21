'''1. Write a Python program to delete the last item from a singly linked list.'''

class Node:  
  
    # Constructor to initialize the node object  
    def __init__(self, data):  
        self.data = data  
        self.next = None
  
def deleteLast(head, key) : 
  
    # Initialize previous of Node to be deleted  
    x = None
  
    # Start from head and find the Node to be  
    # deleted  
    temp = head  
    while (temp != None) : 
      
        # If we found the key, update xv  
        if (temp.key == key) : 
            x = temp  
  
        temp = temp.next
      
    # key occurs at-least once  
    if (x != None) : 
      
        # Copy key of next Node to x  
        x.key = x.next.key  
  
        # Store and unlink next  
        temp = x.next
        x.next = x.next.next
  
        # Free memory for next  
      
    return head 
  
# Utility function to create  
# a new node with given key  
def newNode(key) : 
  
    temp = Node(0)  
    temp.key = key  
    temp.next = None
    return temp  
  
# This function prints contents of linked list  
# starting from the given Node  
def printList( node) : 
  
    while (node != None) : 
      
        print ( node.key, end = " ")  
        node = node.next
      
# Driver Code  
if __name__=='__main__':  
  
    # Start with the empty list  
    head = newNode(1)  
    head.next = newNode(2)  
    head.next.next = newNode(3)  
    head.next.next.next = newNode(5)  
    head.next.next.next.next = newNode(2)  
    head.next.next.next.next.next = newNode(10)  
  
    print("Created Linked List: ")  
    printList(head)  
    deleteLast(head, 2)  
      
    print("\nLinked List after Deletion of 1: ")  
    printList(head) 