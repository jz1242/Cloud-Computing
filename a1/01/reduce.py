#!/usr/bin/env python

import sys

dest_phones = ['2166849356', '4049345110', '5893715037', '9457920329']

def emit(token, count):
    print('{token}\t{count}'.format(token=token, count=count))

previous = None
total = 0
count = 0
for line in sys.stdin:
    line = line.strip() # remove leading and trailing whitespace
    #"{company};{date};{origPhone};{recipPhone};{duration};{count}"
    inputs = line.split(';') # split key-value pair
    try:
        count = int(inputs[5])
    except ValueError:
        continue

    if previous and previous != inputs[0]:
        if total > 0:
            emit(previous, total)
        total = 0
    if inputs[3] in dest_phones:
        total += count
    previous = inputs[0]
if total > 0:
    emit(previous, total)