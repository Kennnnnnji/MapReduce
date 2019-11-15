from __future__ import print_function
import json
from pyspark import SparkContext


def json_prt(line):
    print(json.JSONEncoder().encode(line))


def mapper(row):
    (seqId, nucleotide) = json.loads(row)
    trimmedNucleotide = nucleotide[:-10]
    return [trimmedNucleotide, seqId]


def reducer(id1, id2):
    return None


sc = SparkContext('local', 'test')
textFile = sc.textFile('dna.json')
rdd = textFile.map(mapper)\
    .reduceByKey(reducer) \
    # .flatMap(lambda p_frds: [[p_frds[0], frd] for frd in p_frds[1]])
    # .flatMap(lambda p_frds: [[p_frds[0], frd] for frd in p_frds[1]])
# rdd.foreach(print)
for line in rdd.collect():
    json_prt(line[0])
