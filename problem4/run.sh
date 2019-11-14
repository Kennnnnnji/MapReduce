hadoop fs -rm input/friends4.json
hadoop fs -put /MapReduce/problem4/friends4.json input
hadoop fs -rm output/problem4/*
hadoop fs -rmdir output/problem4
hadoop jar /usr/local/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -D mapred.reduce.tasks=5 -mapper "python /MapReduce/problem4/mapper.py" -reducer " python /MapReduce/problem4/reducer.py " -input input/friends4.json -output output/problem4/
rm result*
hadoop fs -getmerge /user/root/output/problem4 result.txt
