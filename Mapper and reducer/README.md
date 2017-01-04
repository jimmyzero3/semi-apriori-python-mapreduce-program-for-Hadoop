
# Some problems you might encounter using Hadoop

Setting up Hadoop and trying to run a job successfully might be quite frustrating even if you followed all steps in the tutorial, so I'll make a list of possible problems that people might encounter.  
As I only tried Hadoop on my linux machine, these tips are mostly for linux users.  
(I'm currently using hadoop-2.7.3)

##-Java_Home and Hadoop_Home environment variable not set properly.  
Check .bashrc file under your home directory(It's most likely hidden by default), it must contain lines like:  

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
export HADOOP_HOME=/home/hduser/hadoop-2.7.3/hadoop-2.7.3  

But of course, the paths depends on the linux distribution, java and hadoop version you use. 

##-ls: `.': No such file or directory  
When you finally started your Hadoop and can't wait to do $hdfs dfs -ls to see what's in the HDFS, you might get "ls: `.': No such file or directory " from your lovely terminal.  
Don't panic. It's just because there isn't anything in it yet.  
Do $hdfs dfs -mkdir -p /user/[current login user] to make a directory in HDFS and it should be fine.

##-Hadoop streaming failed  
This happens mostly because people forget to make the mapper and reducer file executable.  
Do $sudo chmod +x [mapper file or reducer file] to make them executable.

# Some thoughts on Hadoop
I haven't mastered hadoop for sure, but what I like about it now is it can help us achieve something that our computer can't do with it's native process style.  
For example, I once wrote a quite bad python code which will consume A LOT of memory to do mapreduce jobs, and my 8GB ram wasn't enough.  
Thanks for hadoop, that sloppy code gets to work and gave me the answer I expected.(Sloppy codes won't become good codes just by using Hadoop though.)  
The example above is just one of the advantages of Hadoop. Although some mapreduce job will be done quicker without using hadoop, it might depend on good hardware to achieve.
