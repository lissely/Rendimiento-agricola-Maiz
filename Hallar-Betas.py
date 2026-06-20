import pandas as pd
import numpy as np

df = pd.read_excel("maize.xlsx")

Y = df["Yield_Maize (kg/ha)"].astype(float)
P = df["Precipitation_ANN (mm)"].astype(float)
T = df["Temperature_ANN (°C)"].astype(float)

X = np.column_stack([
    np.ones(len(df)),
    P,
    T,
    P**2,
    T**2,
    P*T
])

beta = np.linalg.inv(X.T @ X) @ X.T @ Y

print("β0 =", beta[0])
print("β1 =", beta[1])
print("β2 =", beta[2])
print("β3 =", beta[3])
print("β4 =", beta[4])
print("β5 =", beta[5])