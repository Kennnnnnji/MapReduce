#!/usr/bin/env python

from __future__ import print_function
import sys
import json

friendsof_a = {}
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the line with json method
    record = json.loads(line)
    a = record[0]
    b = record[1]
    friendsof_a.setdefault(a, set([]))
    if b not in friendsof_a[a]:
        friendsof_a[a].add(b)
        print("%s\t%s" % (a, 1))

