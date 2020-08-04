'''2. Write a Python program to sort a list of elements using the selection sort algorithm.
Note : The selection sort improves on the bubble sort by making only one exchange for every pass through the list. 
Sample Data: [14,46,43,27,57,41,45,21,70]
Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70] '''

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data =[14,46,43,27,57,41,45,21,70]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)