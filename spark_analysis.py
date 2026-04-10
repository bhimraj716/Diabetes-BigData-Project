from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("DiabetesAnalysis") \
    .getOrCreate()

# Load dataset
df = spark.read.csv("diabetes.csv", header=True, inferSchema=True)

# Show first 5 rows
df.show(5)

# Basic analysis
df.groupBy("diabetes").count().show()
df.groupBy("gender").count().show()

# -------------------------------
# Spark SQL 
# -------------------------------

# Register table
df.createOrReplaceTempView("diabetes")

# Query 1: Count diabetes cases
result1 = spark.sql("""
SELECT diabetes, COUNT(*) as count
FROM diabetes
GROUP BY diabetes
""")
result1.show()

# Query 2: Average BMI for diabetic patients
result2 = spark.sql("""
SELECT AVG(bmi) as avg_bmi
FROM diabetes
WHERE diabetes = 1
""")
result2.show()

# Stop Spark 
spark.stop()
