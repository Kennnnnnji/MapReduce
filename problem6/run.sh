hadoop fs -rm input/matrix.json
hadoop fs -put /MapReduce/problem6/matrix.json input
hadoop fs -rm output/problem6/*
hadoop fs -rmdir output/problem6
hadoop jar /usr/local/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -D mapred.reduce.tasks=5 -mapper "python3 /MapReduce/problem6/mapper.py" -reducer " python3 /MapReduce/problem6/reducer.py " -input input/matrix.json -output output/problem6/
rm result*
hadoop fs -getmerge /user/root/output/problem6 result.txt
