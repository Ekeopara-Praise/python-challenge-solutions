'''10. Write a Python program to create a LIFO queue.
Expected Output:
3 2 1 0'''

import queue
q = queue.LifoQueue()
#insert items at the head of the queue 
for x in range(4):
    q.put(str(x))
#remove items from the head of the queue 
while not q.empty():
    print(q.get(), end=" ")
print()
