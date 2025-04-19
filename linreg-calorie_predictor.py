import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv("C:/Users/wasay/Desktop/python/DS-w3/data.csv", header=0, sep=",")

print(full_health_data.head())
print(full_health_data.dtypes)

x = pd.to_numeric(full_health_data["Average_Pulse"], errors='coerce')
y = pd.to_numeric(full_health_data["Calorie_Burnage"], errors='coerce')

full_health_data = full_health_data.dropna(subset=["Average_Pulse", "Calorie_Burnage"])

x = full_health_data["Average_Pulse"]
y = full_health_data["Calorie_Burnage"]

print(f"NaN values in x: {x.isna().sum()}")
print(f"NaN values in y: {y.isna().sum()}")

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y, label="Data points")
plt.plot(x, mymodel, color='red', label="Fitted line")  # Using mymodel here for clarity
plt.ylim(0, 2000)
plt.xlim(0, 200)
plt.xlabel("Average_Pulse")
plt.ylabel("Calorie_Burnage")
plt.legend()
plt.show()

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r**2}")
print(f"P-value: {p}")
print(f"Standard error: {std_err}")
