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

    # parse the input we got from mapper.py
    a, b = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        result.append(a)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        pass


for a in result:
    print(json.JSONEncoder().encode(a))

