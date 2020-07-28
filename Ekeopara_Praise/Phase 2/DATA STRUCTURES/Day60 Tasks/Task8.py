'''8. Write a Python program to find whether a queue is empty or not.
Expected Output:
True
False '''

import queue
p = queue.Queue()
q = queue.Queue()
for x in range(4):
    q.put(x)
print(p.empty())
print(q.empty())

#Reference: w3resource