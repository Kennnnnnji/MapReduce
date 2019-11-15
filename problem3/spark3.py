from __future__ import print_function
import json
from pyspark import SparkContext


def json_prt(line):
    print(json.JSONEncoder().encode(line))


sc = SparkContext('local', 'test')
textFile = sc.textFile('friends.json')
rdd = textFile.map(lambda row: [json.loads(row)[0], [json.loads(row)[1]]]) \
    .reduceByKey(lambda a, b: list(set(a).union(set(b)))) \
    .map(lambda a: [a[0], len(a[1])])

for line in rdd.collect():
    json_prt(line)
