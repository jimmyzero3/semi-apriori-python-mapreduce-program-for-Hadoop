# Python MapReduce Program for Hadoop in Semi-Apriori Style

This is a simple python mapreduce program aiming to find n-K top 100 frequent patterns.  
I'm currently a student studying data science so I tried to make things more comprehensible to other beginners like me.  
  
# Usage

1. Set up a single/multi node Hadoop cluster.  
For beginners, please check Michael G. Noll's [Running Hadoop on Ubuntu Linux (Single-Node Cluster)](http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/) and [Writing an Hadoop MapReduce Program in Python](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/). Those are great tutorials and my code are mostly edit vesion of his.  
Many thanks to him.

2. Run the n1 mapreduce job using Apriori_mapper.py as mapper and Apriori_reducer.py as reducer.

3. If the job is done successfully, download the part-00000 file from your output directory in HDFS.

4. Run $sort -k2 -n -r part-00000 >> [The path you wish]/MapRedSorted_n1_top100, then manually make an top 100 list by deleting lines after line 100. (Come on, don't be lazy.)

5. Repeat step 2 to 4, just remember to change mapper to proper .py file corresponding to the n-K job you are going to do.  
For example, use Apriori_mapper_n2.py for 2-item frequent pattern search. Remember to change your top 100 list name too.(MapRedSorted_n2_top100, MapRedSorted_n3_top100.......)  
Also don't forget to set the file path to your top 100 list in line 9 of every mapper file.
