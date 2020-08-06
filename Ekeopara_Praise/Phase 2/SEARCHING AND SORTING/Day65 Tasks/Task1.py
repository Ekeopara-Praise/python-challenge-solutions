'''
1. Write a Python program to sort a list of elements using Gnome sort.
Gnome sort is a sorting algorithm originally proposed by Dr. Hamid Sarbazi-Azad (Professor of Computer Engineering at Sharif University of Technology) 
in 2000 and called "stupid sort" (not to be confused with bogosort), and then later on described by Dick Grune and named "gnome sort". 
The algorithm always finds the first place where two adjacent elements are in the wrong order, and swaps them.
It takes advantage of the fact that performing a swap can introduce a new out-of-order adjacent pair only next to the two swapped elements. '''

def gnomeSort( arr, n):
   index = 0
   while index < n:
      if index == 0:
         index = index + 1
      if arr[index] >= arr[index - 1]:
         index = index + 1
      else:
         arr[index], arr[index-1] = arr[index-1], arr[index]
         index = index - 1
   return arr
# main
arr = [1,4,2,3,6,5,8,7]
n = len(arr)
arr = gnomeSort(arr, n)
print ("Sorted sequence is:")
for i in arr:
   print (i,end=" ")