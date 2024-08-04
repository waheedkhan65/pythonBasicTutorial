#  The tuple is same as a list, but we can change the item in a list but we can't change the items in a tuple 


tup1 = (1)  # if we write only one number so python take this as a list 
print(type(tup1))

tup2 = (1,) #  Now python take this as a tuple
print(type(tup2))

tup3 = (1, 2, 4, 66, "waheed", "haris", 290, 100)
print (len(tup3))
print (tup3[-4])


if "waheed" in tup3:
    print("Yes waheed is present in this tuple ")
else :
    print("Not in this tuple")   