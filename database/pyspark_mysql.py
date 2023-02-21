from pyspark.sql import SparkSession


def read_data(file: str, spark: SparkSession):
    df_data = spark.read.csv(file, header=True, inferSchema=True)
    df_data.show()


def read_from_mysql_db(spark: SparkSession, user: str, password: str, url: str, db_name: str, table_name: str):
    df = spark.read \
        .format("jdbc") \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .option("url", "jdbc:mysql://" + url + ":3361/" + db_name) \
        .option("dbtable", table_name) \
        .option("user", user) \
        .option("password", password) \
        .load()
    df.show(10)
