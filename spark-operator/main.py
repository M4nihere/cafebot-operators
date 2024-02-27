from pyspark.sql import SparkSession
import time
import json
from pyspark.sql.functions import *
from pyspark.sql.functions import date_format, to_timestamp
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
from datetime import datetime, timedelta
from pyspark.sql.functions import col, from_json
from pyspark.sql.functions import col, to_json, struct
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, IntegerType, FloatType
import time
from pyspark import StorageLevel
import json
spark = SparkSession.builder \
    .appName("ReadFromHive") \
    .enableHiveSupport() \
    .config("spark.hadoop.fs.s3a.access.key", "AKIATPLPFXGCNITXLQIY") \
    .config("spark.hadoop.fs.s3a.secret.key", "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") \
    .config("spark.sql.warehouse.dir", "hdfs://localhost:9000/user/hive/warehouse/") \
    .getOrCreate()

input_path = "s3a://xerberus-nifi-sink/ledger/"
start_time = time.time()
df = spark.read.json(input_path)
df = df.select([df[col_name].cast("string").alias(col_name) for col_name in df.columns])
df = df.withColumn("created_at", date_format(to_timestamp('created_at', 'yyyy-MM-dd HH:mm:ss'), 'yyyy-MM-dd HH:mm:ss'))
df.write.format("org.elasticsearch.spark.sql").option("es.resource", '%s' % ('ledger')).option("es.net.http.auth.user", "elastic").option("es.net.http.auth.pass", "gbEJrOGe_9N5EIm2r5wX").option("es.net.ssl", "true").option("es.nodes","http://57.128.114.235").option("es.batch.size.bytes", "500mb").option("es.port", "9200").option("es.nodes.wan.only","true").mode("append").save()
end_time = time.time()
duration = end_time - start_time
print("#########",duration)