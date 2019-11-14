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
    dnaseq = json.loads(line)
    seqId = dnaseq[0].encode('utf-8')
    nucleotide = dnaseq[1].encode('utf-8')
    trimmedNucleotide = nucleotide[:-10]

    intermediate.setdefault(trimmedNucleotide, [])
    intermediate[trimmedNucleotide].append(seqId)

for key in intermediate:
    print(str(key), end='')
    for v in intermediate[key]:
        print('\t%s' % str(v), end='')
    print()

