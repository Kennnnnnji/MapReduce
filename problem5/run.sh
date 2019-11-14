hadoop fs -rm input/dna.json
hadoop fs -put /MapReduce/problem5/dna.json input
hadoop fs -rm output/problem5/*
hadoop fs -rmdir output/problem5
hadoop jar /usr/local/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -D mapred.reduce.tasks=5 -mapper "python /MapReduce/problem5/mapper.py" -reducer " python /MapReduce/problem5/reducer.py " -input input/dna.json -output output/problem5/
rm result*
hadoop fs -getmerge /user/root/output/problem5 result.txt
