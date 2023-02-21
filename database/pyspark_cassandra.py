from pyspark.sql import SparkSession


def read_data_from_cassandra(spark: SparkSession, url: str, keyspace: str, table_name):
    df = spark.read \
        .format("org.apache.spark.sql.cassandra") \
        .option("spark.cassandra.connection.host",url) \
        .option("keyspace", keyspace) \
        .option("table", table_name) \
        .load()
    df.show(10)