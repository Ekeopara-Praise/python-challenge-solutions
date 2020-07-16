'''3. Write a Python program to map two lists into a dictionary.'''

details = ['Name', 'Age', 'Level']
data = ['Praise', '34', '400']
student_profile = dict(zip(details, data))
print(student_profile)