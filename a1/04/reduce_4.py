#!/usr/bin/env python
import sys

# reverse order for sorting
def emit(token, count):
    print('{count}\t{token}'.format(count=count, token=token))

previous = None
total = 0
count = 0
for line in sys.stdin:
    line = line.strip() # remove leading and trailing whitespace
    #"{company};{origPhone};{recipPhone};{count}"
    inputs = line.split(';') # split key-value pair
    try:
        count = int(inputs[1])
    except ValueError:
        continue

    if previous and previous != inputs[0]:
        emit(previous, total)
        total = 0
    total += count
    previous = inputs[0]

emit(previous, total)