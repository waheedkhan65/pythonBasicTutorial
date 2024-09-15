# # Map is a build-in function and we use this function to apply a function to all values
# num = [1,2,3,4,5,6,7,8]
# squared = list(map(lambda x: x**2, num))
# print(squared)




# # Filter is build-in function and we use this to filter a list 
# num = [1,2,3,4,5,6,7]
# filterAnything = list(filter(lambda x: x%2 != 0, num ))
# print(filterAnything)



# # Sorted is build-in functioin and we use it this for sorting a list, and its ascending order by default
# employ = [("waheed", 23), ("Ahmed", 30), ("Asad", 25), ("Anas", 10)]
# sequence = list(sorted(employ, key=lambda x: x[1]))
# print(sequence)



# # Reduce is a function which we import from functools, its takeS 2 arguments at a time, and thats applies to the give function 
# # cumulatively to the items of a sequence.
# from functools import reduce as rdu
# num = [2,4,6,8,10]
# sum = rdu(lambda x,y: x*y, num)
# print(f"The sum of the numbers is :{sum}")

