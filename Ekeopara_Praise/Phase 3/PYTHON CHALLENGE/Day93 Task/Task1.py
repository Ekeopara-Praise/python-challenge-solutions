'''1. Write a Python program to check if a given string is an anagram of another given string.
Input : 'anagram','nagaram'
Output : True
According to Wikipedia an anagram is direct word switch or word play, the result of rearranging the letters of a word or phrase to produce 
a new word or phrase, using all the original letters exactly once; for example, the word anagram can be rearranged into nag-a-ram '''


s1= str(input("Enter first string:"))
s2= str(input("Enter second string:"))
if(sorted(s1)==sorted(s2)):
      print("True")
else:
      print("False")