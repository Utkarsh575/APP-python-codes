"""
4. School of computing students are planning to design a smart health care wearable device to detect
the mood of the user.
In recent study says, if a person is very relax he will cover the walking distance of 1 kilometer by 15
min, if a person is hectic he will cover the walking distance of 1 kilometer by 9 min and if a person is
normal he will cover the walking distance of 1 kilometer by 12 min.
Based on the covering distance, the system is designed to detect the mood of the user.
input:
Average time taken to cover 1 km: 9min and 30 sec

output:
Mood: hectic
"""

avg_time = str (input ("Enter the Average time taken to cover 1 km (min and sec): "))
mins = int(avg_time[0]+avg_time[1])

if(mins > 12 and mins <=15):
    print("Mood : very relax")
elif mins > 9 and mins <=12:
    print("Mood : Normal")
elif mins <=9 :
    print("Mood : Hectic")


