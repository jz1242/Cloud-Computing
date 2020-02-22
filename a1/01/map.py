#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip() # remove leading and trailing whitespace
    #date, company, orig phone, recip phone, duration
    tokens = line.split(';')
    print("{company};{date};{origPhone};{recipPhone};{duration};{count}".format(
        company=tokens[1], date=tokens[0], origPhone=tokens[2], recipPhone=tokens[3], duration=tokens[4], count=1))