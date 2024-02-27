import sys
from random import random
from operator import add

from pyspark.sql import SparkSession

def run(partitions=2):  # Default value set to 2 if no argument is provided
    spark = SparkSession.builder.appName("CafeBot_Pi").getOrCreate()

    n = 100000 * partitions

    def f(_: int) -> float:
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x * 2 + y * 2 <= 1 else 0

    count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    
    # Print the number of partitions used (either the provided argument or the default value)
    print("Number of partitions:", partitions)
    
    print("Pi is roughly %f" % (4.0 * count / n))

    spark.stop()

# If a command-line argument is provided, use it as the number of partitions
if len(sys.argv) > 1:
    partitions = int(sys.argv[1])
else:
    partitions = 2  # Use a default value if no argument is provided

# Running the Spark application with the specified number of partitions
run(partitions)
