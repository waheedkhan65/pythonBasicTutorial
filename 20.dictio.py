#  Dictionaries in Python
'''
Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value 
pairs that are separated by commas and enclosed within curly brackets {}. 
'''

#  Accessing single values:
stu1 = {"Name": "waheed", 'RollNo': 21, 'Program': "computer science"}
print(stu1)
# print(stu1["name"])
print(stu1.keys())
print("#############################################################################")




# Accessing multiple values:
# We can print all the values in the dictionary using values() method.
for key in stu1.keys():
 print(f"The key is {key} and the value of this key is : {stu1[key]}")
print("#############################################################################")



#  Accessing key-value pairs:
# We can print all the key-value pairs in the dictionary using items() method.
print(stu1.items())
for key, value in stu1.items():
    print(f"The key is {key} and the value is : {value}")
print("#############################################################################")    