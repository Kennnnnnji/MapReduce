#!/usr/bin/env python

from __future__ import print_function
import sys
import json

intermediate = {}

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the line with json method
    record = json.loads(line)
    maxI = 10
    maxJ = 10

    if record[0] == 'a':
        i = record[1]
        for j in range(maxJ + 1):
            intermediate.setdefault((i, j), [])
            intermediate[(i, j)].append(record)
            print('%s,%s' % (i, j), end='\t')
            print(json.JSONEncoder().encode(record))
    elif record[0] == 'b':
        j = record[2]
        for i in range(maxI + 1):
            intermediate.setdefault((i, j), [])
            print('%s,%s' % (i, j), end='\t')
            print(json.JSONEncoder().encode(record))
    else:
        pass

