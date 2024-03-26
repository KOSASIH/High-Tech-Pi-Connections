from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.ml.feature import *

def get_spark_session(app_name):
    """
    Initialize and return a SparkSession object with a given name
    """
    spark = SparkSession.builder \
        .appName(app_name) \
        .master("local[*]") \
        .config("spark.driver.memory", "8g") \
        .config("spark.executor.memory", "8g") \
        .getOrCreate()

    return spark

def process_data(spark, input_file_path, output_file_path):
    """
    Read data, process, and save results using Spark
    """
    # Read input data
    df = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load(input_file_path)

    # Preprocessing
    # Example: Remove NaN values
    df = df.na.drop()

    # Add features if needed, e.g. add a date column
    from pyspark.sql.functions import unix_timestamp
    df = df.withColumn("date", unix_timestamp(df["date_string_column"], "yyyy-MM-dd").cast("date"))

    # Split into train and test datasets
    train_df, test_df = df.randomSplit([0.8, 0.2])

    # Save processed data
    train_df.write.mode("overwrite").format("parquet").save(output_file_path + "/train")
    test_df.write.mode("overwrite").format("parquet").save(output_file_path + "/test")

    return train_df, test_df

def main():
    """
    Initialize Spark, load input data, process it, and generate results
    """
    input_file_path = "path/to/input/big/data"
    output_file_path = "path/to/processed/output/data"

    spark = get_spark_session("Big Data Analytics Example")

    (train_df, test_df) = process_data(spark, input_file_path, output_file_path)

if __name__ == "__main__":
    main()
