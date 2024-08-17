'''
Exception handling in Python is a mechanism to manage errors or "exceptions" that occur during the execution of a 
program. Rather than allowing the program to crash, you can "handle" these exceptions gracefully, providing an 
alternative flow or informative error messages to the user.
'''

num = input("Enter any number for table : ")
print(f"Multiplication table of {num} is : ")
try:
   for i in range (1, 11):
    print(f"{num} x {i} = {int(num)*i}")
except:
  print("Invalid input")
finally:
  print("This will executed always ")
 
 


