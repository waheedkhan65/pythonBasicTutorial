x = 10 
def hello():
    global x 
    x = 100
    y = 20
    print(f"local y {y}")

hello()
print(f"This is global x {x}")    