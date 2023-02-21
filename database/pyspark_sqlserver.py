from pyspark.sql import SparkSession


def read_data_from_sqlserver(spark: SparkSession, url: str, db_name: str, table: str, user: str, password: str):
    df = spark.read \
        .format("jdbc") \
        .option("driver","com.microsoft.sqlserver.jdbc.SQLServerDriver") \
        .option("url", "jdbc:sqlserver://" + url + ":1433;databaseName=" + db_name) \
        .option("dbtable", table) \
        .option("user", user) \
        .option("password", password) \
        .load()
    df.show()