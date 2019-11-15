from __future__ import print_function
import json
from pyspark import SparkContext


def json_prt(line):
    print(json.JSONEncoder().encode(line))


def mapper(row):
    (a, b) = json.loads(row)
    return (a, [b]), (b, [a])


def reducer(list1, list2):
    list1 = set(list1)
    list2 = set(list2)
    intersect = list1.intersection(list2)
    return list1.union(list2) - intersect


sc = SparkContext('local', 'test')
textFile = sc.textFile('friends.json')
rdd = textFile.flatMap(mapper)\
    .reduceByKey(reducer) \
    .flatMap(lambda p_frds: [[p_frds[0], frd] for frd in p_frds[1]])

for line in rdd.collect():
    json_prt(line)
