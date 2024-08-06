tup = ("pakistan", "india", "uk", "china")

temp = list(tup)
temp.append("Russia")
temp.pop(1)
temp[0] = "Pakistan"
tup = tuple(temp) 

print(tup)
