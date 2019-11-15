from __future__ import print_function
from pyspark import SparkContext
import json


def json_prt(lines):
    for line in lines:
        print(json.JSONEncoder().encode(line))


sc = SparkContext('local', 'test')
textFile = sc.textFile("books.json")
inverted = textFile.flatMap(lambda row: [[json.loads(row)[0], word] for word in json.loads(row)[1].split()])\
    .map(lambda file_word: [file_word[1], [file_word[0]]])\
    .reduceByKey(lambda a, b: list(set(a).union(set(b))))  # reduce

for line in inverted.map(lambda x: [x]).collect():
    json_prt(line)
