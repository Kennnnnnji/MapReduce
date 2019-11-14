#!/usr/bin/env python

from __future__ import print_function
import sys
import json

# maps words to their counts
res = []
id2mix = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    id, value = line.split('\t', 1)
    value = value.split('\t')

    # convert count (currently a string) to int
    try:
        id2mix.setdefault(id, [])
        for item in value:
            words = item[1:-2].split('\', \'')
            if 'order' in words[0]:
                id2mix[id] += item[1:-2].split('\', \'')
        for item in value:
            words = item[1:-2].split('\', \'')
            if 'line_item' in words[0]:
                res.append(id2mix[id] + item[1:-2].split('\', \''))
        for i in res:
            for j in range(len(i)):
                i[j] = i[j].replace('\'', '')
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        pass

# write the results to STDOUT (standard output)
for word in res:
    print(json.JSONEncoder().encode(word))

