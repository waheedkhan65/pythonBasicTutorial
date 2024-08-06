import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

if (hour>=0 and hour<13):
    print("Good Morning Sir")
elif (hour>=13 and hour<17):
    print("Good Afternoon Sir")
if  (hour>=17 and hour<0):
    print("Good Evening")