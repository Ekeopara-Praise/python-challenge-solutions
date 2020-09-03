'''3. Write a Python program that takes a text file as input and returns the number of words of a given text file.
Note: Some words can be separated by a comma with no space. '''

def count_words(filepath):
   with open(filepath) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("words.txt"))