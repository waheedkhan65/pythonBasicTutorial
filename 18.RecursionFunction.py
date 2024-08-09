# Recursion Function ia a function which calls itself in order to solve a problem
# Example: 1.Factorial  and 2.Fabonacci
# This function have a two condition 1.Base and 2.Recursion 

# 1. Factorial

def factorial(n):
    if n ==0 or n ==1:
        return 1
    else:
        return n* factorial(n-1)
    
n = int(input("Enter a number to find a factorial : "))
print ("The factorial of ",n,"is :", factorial(n))


# 2. Fabonacci

def fabonacci(n):
    if n == 0 :
     return 0
    elif n == 1:
       return 1
    else :
       return fabonacci(n-1) + fabonacci(n-2)

n = int(input("Enter a number to find its fabonacci sequence : "))
print("The fabonacci sequence of",n,"is :",fabonacci(n))
