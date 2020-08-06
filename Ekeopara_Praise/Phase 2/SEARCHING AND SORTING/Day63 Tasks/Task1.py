'''1. Write a Python program to sort a list of elements using shell sort algorithm.
Note : According to Wikipedia "Shell sort or Shell's method, is an in-place comparison sort. 
It can be seen as either a generalization of sorting by exchange (bubble sort) or sorting by insertion (insertion sort). 
The method starts by sorting pairs of elements far apart from each other, then progressively reducing the gap between elements to be compared. 
Starting with far apart elements can move some out-of-place elements into position faster than a simple nearest neighbor exchange." '''

def shellSort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

data = [9, 8, 3, 7, 5, 6, 4, 1]
size = len(data)
shellSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)