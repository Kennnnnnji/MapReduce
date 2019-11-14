#!/usr/bin/env python

from __future__ import print_function
import sys
import json

# maps words to their counts
resultarr = []
inter = {}
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    # record = json.loads(line)
    (key, value) = line.split('\t')
    (i, j) = key.split(',')
    key = (i, j)
    value = json.loads(value)
    # key = record[0]
    # value = record[1]
    inter.setdefault((key[0], key[1]), [])
    inter[(key[0], key[1])].append(value)

for key in inter:
    values = list(inter[key])
    a_rows = []
    for value in values:
        if value[0] == 'a':
            a_rows.append(value)
    b_rows = []
    for value in values:
        if value[0] == 'b':
            b_rows.append(value)

    result = 0
    for a in a_rows:
        for b in b_rows:
            if (a[2] == b[1]):
                result += a[3] * b[3]

    # emit non-zero results
    if (result != 0):
        resultarr.append((key[0], key[1], result))


for a in resultarr:
    print(json.JSONEncoder().encode(a))
