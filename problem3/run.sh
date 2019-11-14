hadoop fs -put /mapreduce/problem3/friends.json input
hadoop fs -rm output/problem3/*
hadoop fs -rmdir output/problem3
hadoop jar /usr/local/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -D mapred.reduce.tasks=5 -mapper "python /MapReduce/problem3/frdMapper.py" -reducer " python /MapReduce/problem3/frdReducer.py " -input input/friends.json -output output/problem3/
rm result*
hadoop fs -getmerge /user/root/output/problem3 result.txt
