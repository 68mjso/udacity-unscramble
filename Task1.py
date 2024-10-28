"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

result = []

for text in texts:
    if text[0] not in result:
        result.append(text[0])

    if text[1] not in result:
        result.append(text[1])

for call in calls:
    if call[0] not in result:
        result.append(call[0])

    if call[1] not in result:
        result.append(call[1])

print(f"There are {len(result)} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
