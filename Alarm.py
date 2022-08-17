from datetime import datetime
from playsound import playsound
alarm_time=input("enter the time of alarm to be set in HH:MM:SS:am/pm\n")
alarm_hour=alarm_time[0:2]
alarm_min=alarm_time[3:5]
alarm_sec=alarm_time[6:8]
alarm_period=alarm_time[9:11].upper()
print("Alarm is set at{}:{}".format(alarm_hour,alarm_min))
while True:
    now=datetime.now()
    hour=now.strftime("%I")
    min=now.strftime("%M")
    sec=now.strftime("%S")
    time=now.strftime("%p")
    if(alarm_period==time):
        if(alarm_hour==hour):
            if(alarm_min == min):
                if(alarm_sec == sec):
                    print("Wake up buddy")
                
                    break
