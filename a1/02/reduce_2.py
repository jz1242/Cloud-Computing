#!/usr/bin/env python

import sys

def emit(token, count):
    print('{token}\t{count}'.format(token=token, count=count))

previous = None
previous_number = None
total = 0
count = 0
for line in sys.stdin:
    line = line.strip() # remove leading and trailing whitespace
    #"{company};{origPhone};{recipPhone};{count}"
    inputs = line.split(';') # split key-value pair
    try:
        count = int(inputs[3])
    except ValueError:
        continue

    if previous and previous != inputs[0]:
        emit(previous, total)
        total = 0
    if previous_number != inputs[1]:
        total += count
    previous = inputs[0]
    previous_number = inputs[1]

emit(previous, total)