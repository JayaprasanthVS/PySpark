# -*- coding: utf-8 -*-


!pip install pyspark

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataOfSix").getOrCreate()

data = [("Thiru", 19), ("Ram", 20), ("Priya", 21)]
df = spark.createDataFrame(data, ["Name", "Age"])

df.show()
df.printSchema()

!pip install pyspark

from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("DataFrameBasics").getOrCreate()


data = [
    ("Thiru", 19, "CSE"),
    ("Ram", 21, "EEE"),
    ("Kavi", 20, "IT"),
    ("Meena", 22, "CSE"),
    ("Arun", 23, "MECH")
]
columns = ["Name", "Age", "Department"]

df = spark.createDataFrame(data, columns)
df.show()

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType

spark = SparkSession.builder.appName("StructTypeExample").getOrCreate()

student_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("marks", FloatType(), True)
])

student_data = [
    (101, "Jayaprasanth", 87.5),
    (102, "Anjali", 92.0),
    (103, "Rahul", 78.25)
]

df = spark.createDataFrame(student_data, schema=student_schema)

df.show()

df_sorted = df.orderBy("marks", ascending=False)


df_sorted.show()

df_sorted = df.orderBy("id",ascending=True)
df_sorted.show()
