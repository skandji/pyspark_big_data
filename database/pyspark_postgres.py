from pyspark.sql import SparkSession


def read_from_postgres_db(spark: SparkSession, user: str, password: str, url: str, db_name: str, table_name: str):
    df = spark.read \
        .format("jdbc") \
        .option("driver", "org.postgresql.Driver") \
        .option("url", "jdbc:postgresql://" + url + ":5433/" + db_name) \
        .option("dbtable", table_name) \
        .option("user", user) \
        .option("password", password) \
        .load()
    df.show(10)