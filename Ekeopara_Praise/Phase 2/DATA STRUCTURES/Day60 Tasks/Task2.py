'''2. Write a Python program to create a heapsort, pushing all values onto a heap and then popping off the smallest values one at a time.
Expected Output:
[10, 20, 20, 40, 50, 50, 60, 70, 80, 90, 100] '''

import heapq
def heapsort(h):
    heap = []
    for value in h:
        heapq.heappush(heap, value)
    return [heapq.heappop(heap) for i in range(len(heap))]

print(heapsort([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]))

#Reference: w3resource