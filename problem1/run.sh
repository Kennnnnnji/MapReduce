hadoop fs -put /mapreduce/problem1/books.json input
hadoop fs -rm output/problem1/*
hadoop fs -rmdir output/problem1
hadoop jar /usr/local/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -D mapred.reduce.tasks=5 -mapper "python /mapreduce/problem1/python/invertMapper.py" -reducer " python /mapreduce/problem1/python/invertReducer.py " -input input/books.json -output output/problem1/
rm result*
hadoop fs -getmerge /user/root/output/problem1 result.txt
