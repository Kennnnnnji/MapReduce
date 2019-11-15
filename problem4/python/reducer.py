#!/usr/bin/env python

from __future__ import print_function
import sys
import json

# maps words to their counts
result = []

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = line[1:-2].replace('\'', '')

    # parse the input we got from mapper.py
    a, b = line.split(', ', 1)
    # convert count (currently a string) to int
    try:
        result.append((a, b))
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        pass


for word in result:
    print(json.JSONEncoder().encode(word))

