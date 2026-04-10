# Diabetes Big Data Project

##  Project Overview

This project analyzes a real-world healthcare dataset (Diabetes) using Big Data tools.

The project demonstrates how to:

* Store data in MongoDB (NoSQL database)
* Process large datasets using Apache Spark (PySpark)
* Perform queries using Spark SQL and MongoDB Aggregation
* Compare performance between systems
* Visualize insights using graphs

---

##  Technologies Used

* Python
* MongoDB
* PySpark (Apache Spark)
* Matplotlib
* Seaborn
* GitHub

---

##  Project Files

* `insert_data.py` → Insert dataset into MongoDB
* `mongodb_queries.py` → MongoDB queries and aggregation
* `spark_analysis.py` → Data processing using PySpark + Spark SQL
* `visualization.py` → Data visualization (graphs)
* `diabetes.csv` → Dataset

---

##  How to Run the Project

### Step 1: Start MongoDB

Make sure MongoDB is running locally:

```bash
mongod
```

---

### Step 2: Insert Data into MongoDB

```bash
python3 insert_data.py
```

---

### Step 3: Run MongoDB Queries

```bash
python3 mongodb_queries.py
```

---

### Step 4: Run Spark Analysis

```bash
python3 spark_analysis.py
```

---

### Step 5: Run Visualization

```bash
python3 visualization.py
```

---

##  Output

* Data inserted into MongoDB
* Query results (counts, averages)
* Spark SQL results
* Performance comparison
* Graphs (Diabetes distribution, BMI vs Glucose)

---

##  Dataset

Diabetes dataset in CSV format used for healthcare analysis.

Dataset Link: https://www.kaggle.com/datasets/priyamchoksi/100000-diabetes-clinical-dataset

---

##  Conclusion

This project demonstrates the integration of MongoDB and Apache Spark for efficient big data processing and analysis.
