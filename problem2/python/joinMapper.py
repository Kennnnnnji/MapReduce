#!/usr/bin/env python

from __future__ import print_function
import sys
import json

intermediate = {}   # order/line id: value
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.encode('utf-8')
    line = line.strip().encode('utf-8')

    # parse the line with json method
    record = json.loads(line)
    order_id = record[1]
    value = record
    for i in range(len(record)):
        value[i] = value[i].encode('utf-8')
    # add line to order
    intermediate.setdefault(order_id, [])
    intermediate[order_id].append(value)

    # print('%s\t%s' % (order_id, value))

for id in intermediate:
    print(id.encode('utf-8'), end='')
    for v in intermediate[id]:
        print('\t%s' % v, end='')
    print()
