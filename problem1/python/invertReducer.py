#!/usr/bin/env python
from __future__ import print_function
import sys
import json

# maps words to their counts
word2fileNames = {}
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    word, fileName = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        if word not in word2fileNames:
            word2fileNames[word] = []
        if fileName not in word2fileNames[word]:
            word2fileNames[word].append(fileName)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        pass

# write the results to STDOUT (standard output)
for word in word2fileNames:
    print(json.JSONEncoder().encode([word, word2fileNames[word]]))
