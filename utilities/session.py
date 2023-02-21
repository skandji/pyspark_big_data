from pyspark.sql import SparkSession


def spark_session():
    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("Mon application Spark") \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .config("spark.sql.crossJoin.enabled", "true") \
        .getOrCreate()
    return spark
