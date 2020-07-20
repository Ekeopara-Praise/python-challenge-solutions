'''9. Write a Python program to store a given dictionary in a json file.
Original dictionary:
{'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
<class 'dict'>
Json file to dictionary:
{'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}'''

import json


dict = {"member #002":{"first name": "John", "last name": "Doe", "age": 34},
        "member #003":{"first name": "Elijah", "last name": "Baley", "age": 27},
        "member #001":{"first name": "Jane", "last name": "Doe", "age": 42}}


with open('data.json', 'w') as fp:
    json.dump(dict, fp,  indent=4)