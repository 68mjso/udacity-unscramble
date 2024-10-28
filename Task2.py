"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""

import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

result = []
result_time = []

for call in calls:
    time = int(call[3])
    index = -1
    if call[0] in result:
        index = result.index(call[0])
        result_time[index] += time
    else:
        result.append(call[0])
        result_time.append(time)
    if call[1] in result:
        index = result.index(call[1])
        result_time[index] += time
    else:
        result.append(call[1])
        result_time.append(time)

temp = result_time
temp.sort(reverse=True)

index = result_time.index(temp[0])

print(
    f"{result[index]} spent the longest time, {temp[0]} seconds, on the phone during September 2016."
)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
