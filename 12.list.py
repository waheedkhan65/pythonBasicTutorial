lst = [2, 3, 5, "waheed", "khan", 10, 55, 100, 99]
print (type(lst))
print(lst[1:])
print(lst[1:9:2])
# the below line will give error because 9 is length not location 
# print(lst[9])
if "waheed" in lst:
    print("Yes")
else:
    print("No") 