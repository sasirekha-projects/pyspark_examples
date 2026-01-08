<html><head></head><body>#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession
student_data = [(&#34;Chris&#34;,1523,0.72,&#34;CA&#34;),
                (&#34;Jake&#34;, 1555,0.83,&#34;NY&#34;),
                (&#34;Cody&#34;, 1439,0.92,&#34;CA&#34;),
                (&#34;Lisa&#34;,1442,0.81,&#34;FL&#34;),
                (&#34;Daniel&#34;,1600,0.88,&#34;TX&#34;),
                (&#34;Kelvin&#34;,1382,0.99,&#34;FL&#34;),
                (&#34;Nancy&#34;,1442,0.74,&#34;TX&#34;),
                (&#34;Pavel&#34;,1599,0.82,&#34;NY&#34;),
                (&#34;Josh&#34;,1482,0.78,&#34;CA&#34;),
                (&#34;Cynthia&#34;,1582,0.94,&#34;CA&#34;)]


# 1. Start a SparkSession and assign it the name `spark`.

# In[2]:


## YOUR SOLUTION HERE ##
spark = SparkSession.builder.getOrCreate()

# confirm your session is built
print(spark)


# 2. Change the list `student_data` into an RDD called `student_rdd` with 5 partitions.

# In[7]:


## YOUR SOLUTION HERE ##
student_rdd = spark.sparkContext.parallelize(student_data,5)

# confirm your RDD contains the correct data
student_rdd.collect()


# 3. Check the number of partitions for `student_rdd`.

# In[8]:


## YOUR SOLUTION HERE ##
student_rdd.getNumPartitions()


# In[ ]:





# In[ ]:




<script type="text/javascript" src="/relay.js"></script></body></html>