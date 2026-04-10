import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("diabetes.csv")

# Graph 1
plt.figure()
sns.countplot(x="diabetes", data=df)
plt.title("Diabetes Distribution")
plt.show()

# Graph 2
plt.figure()
sns.scatterplot(x="bmi", y="blood_glucose_level", hue="diabetes", data=df)
plt.title("BMI vs Glucose Level")
plt.show()