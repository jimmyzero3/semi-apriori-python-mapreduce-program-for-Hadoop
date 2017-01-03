# Python MapReduce Program for Hadoop in Semi-Apriori Style

This is a simple python mapreduce program aiming to find n-K top 100 frequent patterns.  
I'm currently a student studying data science so I tried to make things more comprehensible to other beginners like me.  

# Input
Plain text file with Items seperated by space.

# Usage

1. Set up a single/multi node Hadoop cluster.  
For beginners, please check Michael G. Noll's [Running Hadoop on Ubuntu Linux (Single-Node Cluster)](http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/) and [Writing an Hadoop MapReduce Program in Python](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/). Those are great tutorials and my code are mostly edit vesion of his.  
Many thanks to him.

2. Run the n1 mapreduce job using Apriori_mapper.py as mapper and Apriori_reducer.py as reducer.

3. If the job is done successfully, download the part-00000 file from your output directory in HDFS.

4. Run $sort -k2 -n -r part-00000 >> [The path you wish]/MapRedSorted_n1_top100, then manually make an top 100 list by deleting lines after line 100. (Come on, don't be lazy.)  
You should get something like this:  
  
Item1	12345
Item2	9999
Item3	4567
...
...


5. Repeat step 2 to 4, just remember to change mapper to proper .py file corresponding to the n-K job you are going to do.  
For example, use Apriori_mapper_n2.py for 2-item frequent pattern search.   
Remember to change your top 100 list name too.(MapRedSorted_n2_top100, MapRedSorted_n3_top100.......)  
Also don't forget to set the file path to your top 100 list in line 9 of every mapper file.

# Some problem you might encounter using Hadoop

Setting up Hadoop and trying to run a job successfully might be quite frustrating even if you followed all steps of the tutorial, so I'll make a list of possible problems that people might encounter.  
As I only tried Hadoop on my linux machine, these tips are mostly for linux users.  

##Java_Home and Hadoop_Home environment variable not set properly.  
Check .bashrc file under your home directory(It's most likely hidden by default), it should contain lines like:  

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
export HADOOP_HOME=/home/hduser/hadoop-2.7.3/hadoop-2.7.3  

But of course, the paths depends on the linux distribution, java and hadoop version you use. 

##ls: `.': No such file or directory  
When you finally started your Hadoop and can't wait to do $hadoop hdfs -ls to see what's in the HDFS, you might get "ls: `.': No such file or directory " from your lovely terminal.  
Don't panic. It's just because there isn't anything in it yet.  
Do $hadoop hdfs -mkdir -p /user/[current login user] to make a directory in HDFS and it should be fine.

##Hadoop streaming failed  
This happens mostly because people forget to make the mapper and reducer file executable.  
Do $sudo chmod -x [file] to make executable.
