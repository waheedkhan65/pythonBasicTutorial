''' The enumerate() function in Python adds a counter to an iterable (like a list, tuple, or string) and returns it as an enumerate
 object. This can be particularly useful when you need both the index and the value of elements in a loop.'''


list = ["Orange", "Cherry", "watermelon", "Apple"]

for index, fruit in enumerate(list,start=1):
 print(index, fruit)