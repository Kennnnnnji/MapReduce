#!/usr/bin/env python

import sys
import json

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the line with json method
    record = json.loads(line)
    fileName = record[0]
    value = record[1]

    # split the line into words
    words = value.split()

    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print('%s\t%s' % (word, fileName))
