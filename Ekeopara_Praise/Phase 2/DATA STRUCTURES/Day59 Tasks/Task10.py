'''10. Write a Python program to push three items into a heap and return the smallest item from the heap. Also Pop and return the smallest item from the heap.
Expected Output:
Items in the heap:
('V', 1)
('V', 3)
('V', 2)
----------------------
The smallest item in the heap:
('V', 1)
----------------------
Pop the smallest item in the heap:
('V', 2)
('V', 3) '''

import heapq
heap = []
heapq.heappush(heap, ('V', 3))
heapq.heappush(heap, ('V', 2))
heapq.heappush(heap, ('V', 1))
print("Items in the heap:")
for a in heap:
	print(a)
print("----------------------")
print("The smallest item in the heap:")
print(heap[0])
print("----------------------")
print("Pop the smallest item in the heap:")
heapq.heappop(heap)
for a in heap:
	print(a)

#Reference: w3resource