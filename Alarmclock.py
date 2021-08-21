#Alarm Clock
from datetime import datetime
import urllib
import webbrowser
time=input("ENter the alarm time : HH:MM:SS ")
hour = time[0:2]
minu = time[3:5]
sec=   time[6:8]
print("Setting your alarm")
while True:
    now = datetime.now()
    curr_hour = now.strftime("%H")
    curr_min = now.strftime("%M")
    curr_sec = now.strftime("%S")
    if(hour == curr_hour):
        if(minu == curr_min):
            if(sec == curr_sec):
                print("Wakeup Sid")
                webbrowser.open("https://www.youtube.com/watch?v=iNpXCzaWW1s")
                break
