hadoop fs -put /mapreduce/problem2/records.json input
hadoop fs -rm output/problem2/*
hadoop fs -rmdir output/problem2
hadoop jar /usr/local/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -D mapred.reduce.tasks=5 -mapper "python /mapreduce/problem2/joinMapper.py" -reducer " python /mapreduce/problem2/joinReducer.py " -input input/records.json -output output/problem2/
rm result*
hadoop fs -getmerge /user/root/output/problem2 result.txt
