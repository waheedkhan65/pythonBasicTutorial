# In python, we can raise custom errors by using the raise keyword.



#          *****Built-in Exceptions*****

# salary = int(input("Enter your salary :"))
# if salary> 5000 or salary<2000:
#  raise ValueError("Not a correct salary")
# else:
#  print(f"Your salary is {salary}")


#         *****Inheriting from built-in exceptions*****

# class customSalaryError (Exception):
#  pass
# def checkSalary(x):
#   if x > 5000 or x < 2000:
#    raise customSalaryError("Salary is not Correct")

# try:
 
#  salary = input("Enter your salary : ")
#  if salary.lower() == "quit":
#    print("The program is quit")
#  else:
#    salary = int(salary)
#    checkSalary(salary)
#    print(f"The salary is : {salary}")

# except customSalaryError as w:
#  print(w)
 
# except ValueError:
#  print("Please enter valid value")

 