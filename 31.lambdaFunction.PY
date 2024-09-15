# # Lambda is build in Function which we is Anonymous, short, and one-Line function.

# num = int(input("Enter any Number for cube: "))
# cube = lambda x: x*x*x
# print(f"The cube of {num} is: ", cube(num))



# # Example of lambda as a in line 
# num = int(input("Enter a number : "))
# print(f"The Squared of a {num} is : ",(lambda x: x**2)(num))


# Example of passing a function into a function
# def apply(fc, value):
#     return 2 + fc(value)

# num = int(input("Enter a Number : "))
# cube = lambda x: x*x*x 
# print(f"The number {num} is became : {apply(cube,num)}")


# #  Or we can also write the above program like the below one
# def apply(fc, value):
#     return 2 + fc(value)

# num = int(input("Enter a Number : "))
# print(f"The number {num} is : {apply(lambda x: x*x*x, num)}")