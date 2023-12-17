import time
import datetime as date
x = date.date
print(x)
timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print("Current Time is ", timestamp)
if(hour< 12 and hour>= 0):
    print("Good Morning, Sir")
elif(hour>=12 and hour<17):
    print("God Afternoon, Sir")
else:
    print("Good Night, Sir")