import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName("MyApp").getOrCreate()

X = pd.DataFrame({"x_1": [1, 1, 2, 2], "x_2":[1, 2, 2, 3]})
y = np.dot(X, np.array([1, 2])) + 3
reg = LinearRegression().fit(X, y)

# define our predict function
def predict(df: pd.DataFrame, model: LinearRegression) -> pd.DataFrame:
    """
    Function to predict results using a pre-built model
    """
    return df.assign(predicted=model.predict(df))

# create test data
input_df = pd.DataFrame({"x_1": [3, 4, 6, 6], "x_2":[3, 3, 6, 6]})

# test the predict function
predict(input_df, reg)

# import Fugue
from fugue import transform

# use Fugue transform to switch exection to spark
result = transform(
    df=input_df,
    using=predict,
    schema="*,predicted:double",
    params=dict(model=reg),
    engine=spark
)

# result is a Spark DataFrame
print(type(result))
result.show()

