#!/usr/bin/env python

import sys

spam_company = []
# Get all spam companies
f = open("spam.txt", "r")
for line in f:
    line = line.strip()
    tokens = line.split('\t')
    spam_company.append(tokens[0])

for line in sys.stdin:
    line = line.strip() # remove leading and trailing whitespace
    #date, company, orig phone, recip phone, duration
    tokens = line.split(';')

    if tokens[1] in spam_company:
        print("{origPhone};{count}".format(
            origPhone=tokens[2], count=1))