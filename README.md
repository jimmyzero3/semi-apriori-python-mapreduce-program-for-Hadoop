# Python MapReduce Program for Hadoop in Semi-Apriori Style

This is a simple python mapreduce program aiming to find n-K top 100 frequent patterns.  
I'm currently a student studying data science so I tried to make things more comprehensible to other beginners like me.  

# Input
Plain text file with Items seperated by space.

# Usage

1. Set up a single/multi node Hadoop cluster.  
For beginners, please check Michael G. Noll's [Running Hadoop on Ubuntu Linux (Single-Node Cluster)](http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/) and [Writing an Hadoop MapReduce Program in Python](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/). Those are great tutorials and my code are mostly edit version of his.  
Many thanks to him.

2. Do $sudo chmod +x [all mapper and reducer files] to make them executable.

3. Run the n1 mapreduce job on Hadoop using Apriori_mapper.py as mapper and Apriori_reducer.py as reducer.

4. If the job is done successfully, download the part-00000 file from your output directory in HDFS.

5. Run $sort -k2 -n -r part-00000 >> [The path you wish]/MapRedSorted_n1_top100, then manually make a top 100 list by deleting lines after line 100. (Come on, don't be lazy.)  
You should get something like this:  
  
Item1&nbsp;&nbsp;&nbsp;&nbsp;12345  
Item2&nbsp;&nbsp;&nbsp;&nbsp;9999  
Item3&nbsp;&nbsp;&nbsp;&nbsp;4567  
...  
...  
  

5. Repeat step 2 to 4, just remember to change mapper to proper .py file corresponding to the n-K job you are going to do.  
For example, use Apriori_mapper_n2.py for 2-item frequent pattern search.   
Remember to change your top 100 list name too.(MapRedSorted_n2_top100, MapRedSorted_n3_top100.......)  
Also don't forget to set the file path to your top 100 list in line 9 of every mapper file.

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
