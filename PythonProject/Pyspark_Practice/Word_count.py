# import os
# os.environ["JAVA_HOME"] = r"C:\Program Files\Eclipse Adoptium\jdk-8.0.472.8-hotspot\bin\java.exe"
from platform import java_ver
from string import whitespace

from pyspark.sql import SparkSession
from unicodedata import normalize

spark= SparkSession.builder.appName("practice_session").getOrCreate()


"""
Hello world
Hello Spark
Spark is Fast
Hello world world
"""

# Create sparkContext to deal with rdd
sc=spark.sparkContext

#input the lines
# Create an RDD

line=[
"Hello world",
"Hello Spark",
"Spark is Fast",
"Hello world world"
]
rdd=sc.parallelize(line)

print("partitions:",rdd.getNumPartitions())

# Tokenize by whitespace, normalize to lowercase
words= rdd.flatMap(lambda line: line.split(" "))
print(words.collect())
# Compute word count sorted by descending count, then ascending word
