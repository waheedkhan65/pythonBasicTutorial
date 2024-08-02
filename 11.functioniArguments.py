'''
There are four types of arguments that we can provide in a function:

1. Default Arguments
2. Keyword Arguments
3. Variable length Arguments
4. Required Arguments

1. We can provide a default value while creating a function. This way the function assumes a default value even if a value is 
not provided in the function call for that argument.

2. We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, 
the the order in which the arguments are passed does not matter.

3. Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length 
arguments

4. In case we do not pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct 
positional order and the number of arguments passed should match with actual function definition.

'''
# 1 wla example
def average(a=4, b=6):
    print("The average is :", a+b/2)
average()

# 2 wla example
def mult(a,b):
    print("The multiple of two numbers is : ", a*b)
mult(b=5,a=3)

# 4 wla example
def  name(fName, mName, lName):
    print("Hello", fName,mName,lName)
name("waheed","Ur","Rahman")    
