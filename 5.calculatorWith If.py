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

elif (num == 2):
  print ("The value of",a,"-",b,"is = ",sub(a,b))

elif (num == 3): 
 print ("The value of",a,"/",b,"is = ",div(a,b))

elif (num == 4):
 print ("The value of",a,"x",b,"is = ",mult(a,b))

else:
  print("invalid input , Please choose a number between 1 and 4. ")
  continue

