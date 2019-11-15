#!/usr/bin/env python

from __future__ import print_function
import sys
import json

friendsof_a = {}
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().encode('utf-8')

    # parse the line with json method
    record = json.loads(line)
    a = record[0].encode('utf-8')
    b = record[1].encode('utf-8')

    friendsof_a.setdefault(a, set([]))
    if b not in friendsof_a[a]:
        friendsof_a[a].add(b)

result = []
for i in friendsof_a:
    for j in friendsof_a[i]:
        if j in friendsof_a and i not in friendsof_a[j] or j not in friendsof_a:
            result.append((i, j))
            result.append((j, i))

for word in result:
    print(word)
