'''1. Write a Python program to sort a list of elements using the bubble sort algorithm.
Note : According to Wikipedia "Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through 
the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. 
The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. 
The algorithm, which is a comparison sort, is named for the way smaller elements "bubble" to the top of the list.
Although the algorithm is simple, it is too slow and impractical for most problems even when compared to insertion sort.
It can be practical if the input is usually in sort order but may occasionally have some out-of-order elements nearly in position."

Sample Data: [14,46,43,27,57,41,45,21,70]
Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70] '''

a = [14,46,43,27,57,41,45,21,70]

#repeating loop len(a)(number of elements) number of times
for j in range(len(a)):
    #initially swapped is false
    swapped = False
    i = 0
    while i<len(a)-1:
        #comparing the adjacent elements
        if a[i]>a[i+1]:
            #swapping
            a[i],a[i+1] = a[i+1],a[i]
            #Changing the value of swapped
            swapped = True
        i = i+1
    #if swapped is false then the list is sorted
    #we can stop the loop
    if swapped == False:
        break
print (a)
