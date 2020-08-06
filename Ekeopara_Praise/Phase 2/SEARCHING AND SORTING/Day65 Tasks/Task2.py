'''2. Write a Python program to sort a list of elements using Cocktail shaker sort.
From Wikipedia, Cocktail shaker sort,[1] also known as bidirectional bubble sort,[2] cocktail sort, 
shaker sort (which can also refer to a variant of selection sort), ripple sort, shuffle sort,[3] or shuttle sort,
is a variation of bubble sort that is both a stable sorting algorithm and a comparison sort.
The algorithm differs from a bubble sort in that it sorts in both directions on each pass through the list.
This sorting algorithm is only marginally more difficult to implement than a bubble sort, and solves the problem of turtles in bubble sorts. 
It provides only marginal performance improvements, and does not improve asymptotic performance; 
like the bubble sort, it is not of practical interest (insertion sort is preferred for simple sorts), though it finds some use in education.'''

def cocktailSort(a): 
    n = len(a) 
    swapped = True
    start = 0
    end = n-1
    while (swapped == True): 
        # reset the swapped flag on entering the loop, 
        # because it might be true from a previous 
        # iteration. 
        swapped = False
        # loop from left to right same as the bubble 
        # sort 
        for i in range (start, end): 
            if (a[i] > a[i + 1]) : 
                a[i], a[i + 1]= a[i + 1], a[i] 
                swapped = True
        # if nothing moved, then array is sorted. 
        if (swapped == False): 
            break
        # otherwise, reset the swapped flag so that it 
        # can be used in the next stage 
        swapped = False
        # move the end point back by one, because 
        # item at the end is in its rightful spot 
        end = end-1
        # from right to left, doing the same 
        # comparison as in the previous stage 
        for i in range(end-1, start-1, -1): 
            if (a[i] > a[i + 1]): 
                a[i], a[i + 1] = a[i + 1], a[i] 
                swapped = True
        # increase the starting point, because 
        # the last stage would have moved the next 
        # smallest number to its rightful spot. 
        start = start + 1
# Driver code to test above 
a = [6 ,2 ,5 ,3 ,9 ,1, 3 ] 
cocktailSort(a) 
print("Sorted array is:") 
for i in range(len(a)): 
    print ("% d" % a[i])