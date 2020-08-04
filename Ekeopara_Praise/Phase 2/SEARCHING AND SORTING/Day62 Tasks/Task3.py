'''3. Write a Python program to sort a list of elements using the insertion sort algorithm.
Note : According to Wikipedia "Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort."
Sample Data: [14,46,43,27,57,41,45,21,70]
Expected Result : [14, 21, 27, 41, 43, 45, 46, 57, 70]'''

a = [14,46,43,27,57,41,45,21,70]

#iterating over a
for i in a:
    j = a.index(i)
    #i is not the first element
    while j>0:
        #not in order
        if a[j-1] > a[j]:
            #swap
            a[j-1],a[j] = a[j],a[j-1]
        else:
            #in order
            break
        j = j-1
print (a)