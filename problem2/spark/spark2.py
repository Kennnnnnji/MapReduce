from __future__ import print_function
from pyspark import SparkContext
import json


def json_prt(line):
    print(json.JSONEncoder().encode(line))


def merge(a):
    for line in a[1][1:]:
        yield a[1][0] + line


sc = SparkContext('local', 'test')
textFile = sc.textFile('records.json')
rdd = textFile.map(lambda row: [json.loads(row)[1], [json.loads(row)]]) \
    .reduceByKey(lambda a, b: a + b) \
    .flatMap(merge)

for line in rdd.collect():
    json_prt(line)
