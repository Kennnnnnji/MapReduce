from __future__ import print_function
import json
from pyspark import SparkContext


def json_prt(line):
    print(json.JSONEncoder().encode(line))


def mapper(line):
    line = line.strip()
    record = json.loads(line)
    maxI = 10
    maxJ = 10
    ret = []
    if record[0] == 'a':
        i = record[1]
        for j in range(maxJ + 1):
            ret.append([(i, j), record])
    elif record[0] == 'b':
        j = record[2]
        for i in range(maxI + 1):
            ret.append([(i, j), record])
    else:
        pass
    return ret


def reducer(line):
    record = line  # json.loads(line)
    key = record[0]
    values = record[1]

    values = list(values)
    a_rows = list(filter(lambda x: x[0] == 'a', values))
    b_rows = list(filter(lambda x: x[0] == 'b', values))

    result = 0
    for a in a_rows:
        for b in b_rows:
            if (a[2] == b[1]):
                result += a[3] * b[3]
    if (result != 0):
        return ((key[0], key[1], result))


sc = SparkContext('local', 'test')
textFile = sc.textFile('matrix.json')
rdd = textFile.flatMap(mapper) \
    .groupByKey() \
    .map(reducer)

for line in rdd.collect():
    if line != None:
        json_prt(line)
