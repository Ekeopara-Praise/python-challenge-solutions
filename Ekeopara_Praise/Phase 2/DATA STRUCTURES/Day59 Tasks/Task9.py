'''9. Write a Python program to push three items into the heap and print the items from the heap.
Expected Output:
('V', 1)
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