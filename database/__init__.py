import pyspark_mysql
import pyspark_postgres
import pyspark_cassandra
import pyspark_sqlserver
import utilities.session as s

spark = s.spark_session()
# pyspark_mysql.read_from_mysql_db(spark, "root", "PassWord23!", "127.0.0.1", "spark_order_db", "orders")
# pyspark_postgres.read_from_postgres_db(spark, "consult", "PassWord23!", "127.0.0.1", "jea_db", "orders")
pyspark_sqlserver.read_data_from_sqlserver(spark, "localhost", "jea_db", "orders", "sa", "PassWord23!")
# pyspark_cassandra.read_data_from_cassandra(spark, "localhost", "jea_db", "orders")
