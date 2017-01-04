# Python MapReduce Program for [Hadoop](http://hadoop.apache.org/releases.html) in Semi-Apriori Style

This is a simple python mapreduce program aiming to find n-K top 100 frequent patterns.  
I'm currently a student studying data science so I tried to make things more comprehensible to other beginners like me.  

# Input
Plain text file with Items seperated by space.

#Configuration
No special configs needed, only some path changes in python file and renaming output files(Check step 5 and 6 in usage.)

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
  

6. Repeat step 2 to 4, just remember to change mapper to proper .py file corresponding to the n-K job you are going to do.  
For example, use Apriori_mapper_n2.py for 2-item frequent pattern search.   
Remember to change your top 100 list name too.(MapRedSorted_n2_top100, MapRedSorted_n3_top100.......)  
Also don't forget to set the file path to your top 100 list in line 9 of every mapper file.
