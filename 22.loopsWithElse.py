# Yes we can use else with forloop and whileloop
# but here is example to clear the concept that how ?

# is we write the else with forLoop and whileLoop the "Else" will executed after the loop id fully executed 
# w = 1
# for w in range (10):
#     print(f"2 X {w+1} = {(w+1)*2} ")
# else:
#     print("Now loop is executed and the Else is also run")    


# but if we write the above code as it is and include if and only break between the loop and else so the else will not 
# run 

i = 1
for i in range (10):
     print(f"2 x {i+1} = {(i+1)*2}")
     if i == 4:  
       break
else:
    print("Now loop is executed and the Else is also run")        

