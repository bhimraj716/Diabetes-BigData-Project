from pymongo import MongoClient
import time

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["diabetes_db"]
collection = db["patients"]

# 1. Count total records
total = collection.count_documents({})
print("Total records:", total)

# 2. Count diabetic vs non-diabetic
pipeline1 = [
    {"$group": {"_id": "$diabetes", "count": {"$sum": 1}}}
]
result1 = list(collection.aggregate(pipeline1))
print("Diabetes distribution:", result1)

# 3. Average BMI of diabetic patients
pipeline2 = [
    {"$match": {"diabetes": 1}},
    {"$group": {"_id": None, "avg_bmi": {"$avg": "$bmi"}}}
]
result2 = list(collection.aggregate(pipeline2))
print("Average BMI (diabetic):", result2)

# 4. Average glucose level
pipeline3 = [
    {"$group": {"_id": None, "avg_glucose": {"$avg": "$blood_glucose_level"}}}
]
result3 = list(collection.aggregate(pipeline3))
print("Average glucose:", result3)

# ===============================
# Performance Comparison (ADD THIS)
# ===============================
start = time.time()
list(collection.aggregate([
    {"$group": {"_id": "$diabetes", "count": {"$sum": 1}}}
]))
print("MongoDB execution time:", time.time() - start)