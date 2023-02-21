from pyspark.sql import SparkSession


def read_from_csv(spark: SparkSession, delimiter: str, header: bool, file: str):
    data_frame = spark.read\
        .format("com.databricks.spark.csv")\
        .option("delimiter", delimiter)\
        .option("header", header)\
        .load(file)
    return data_frame


def read_from_csv_with_schema(spark: SparkSession, delimiter: str, header: bool, file: str, schema):
    data_frame = spark.read \
        .format("com.databricks.spark.csv") \
        .option("delimiter", delimiter) \
        .option("header", header) \
        .schema(schema)\
        .load(file)
    return data_frame