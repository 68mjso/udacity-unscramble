"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

text_arr_0 = []
text_arr_1 = []
for item in texts:
    text_arr_0.append(item[0])
    text_arr_1.append(item[1])
tele_arr = []
for item in calls:
    if (
        item[0].startswith("140")
        and item[0] not in tele_arr
        and item[0] not in text_arr_0
        and item[0] not in text_arr_1
    ):
        tele_arr.append(item[0])
print("These numbers could be telemarketers:")
for item in tele_arr:
    print(item)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

