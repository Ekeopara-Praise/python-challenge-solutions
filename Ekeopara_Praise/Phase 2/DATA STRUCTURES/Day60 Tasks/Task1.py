'''
1. Write a Python program to push an item on the heap, then pop and return the smallest item from the heap.
Expected Output:
Items in the heap:
('V', 1)
('V', 3)
('V', 2)
----------------------
Using heappushpop push item on the heap and return the smallest item.
('V', 2)
('V', 3)
('V', 6) '''

import heapq
heap = []
heapq.heappush(heap, ('V', 3))
heapq.heappush(heap, ('V', 2))
heapq.heappush(heap, ('V', 1))
print("Items in the heap:")
for a in heap:
	print(a)
print("----------------------")
print("Using heappushpop push item on the heap and return the smallest item.")
heapq.heappushpop(heap, ('V', 6))
for a in heap:
	print(a)
