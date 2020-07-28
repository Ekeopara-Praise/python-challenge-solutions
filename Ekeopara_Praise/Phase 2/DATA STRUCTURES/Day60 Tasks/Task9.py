'''9. Write a Python program to create a FIFO queue.
Expected Output:
0 1 2 3 '''

import queue
q = queue.Queue()
#insert items at the end of the queue 
for x in range(4):
    q.put(str(x))
#remove items from the head of the queue 
while not q.empty():
    print(q.get(), end=" ")
print("\n")