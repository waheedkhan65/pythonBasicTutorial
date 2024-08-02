# The code will show simple calculation on two numbers 
a = int(input ("Enter first number : " ))
b = int(input ("Enter first number : " )) 
 
def add (a , b):
    return a + b
def sub (a , b):
 return a - b
def div (a , b):
  if (b==0):
   return ("Error! cannot divide by zero")
  else:
   return a / b
def mult (a , b):
   return a * b

num = int(input("Enter number of operation what you want\n 1. adding \n 2. subtraction \n 3. division \n 4. multiplication \n " , ))  

if (num == 1):
 print ("The value of",a,"+",b,"is = ",add(a,b))

if (num == 2):
 print ("The value of",a,"-",b,"is = ",sub(a,b))

if (num == 3):
 print ("The value of",a,"/",b,"is = ",div(a,b))

if (num == 4):
 print ("The value of",a,"x",b,"is = ",mult(a,b))


