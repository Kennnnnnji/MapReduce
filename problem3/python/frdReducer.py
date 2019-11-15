#!/usr/bin/env python

from __future__ import print_function
import sys
import json

# maps words to their counts
name2cnt = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    a, cnt = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        name2cnt.setdefault(a, 0)
        name2cnt[a] += int(cnt)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        pass

# write the results to STDOUT (standard output)
for word in name2cnt:
    print(json.JSONEncoder().encode([word, name2cnt[word]]))

