import pandas as pd

# Vytvoření jednoduchého datasetu
data = {
    "age": [22, 25, 30, 35, 40, 45],
    "salary": [25000, 28000, 35000, 40000, 45000, 50000]
}
df = pd.DataFrame(data)
print(df)

X = df[["age"]]  # vstupní proměnná (věk)
y = df["salary"]  # výstupní proměnná (plat)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)

# Predikce pro věk 32
predicted_salary = model.predict(pd.DataFrame([[32]], columns=["age"]))
print(f"Predikovaný plat pro věk 32: {predicted_salary[0]:.2f}")

print(f"Sklon (a): {model.coef_[0]:.2f}")
print(f"Intercept (b): {model.intercept_:.2f}")

import matplotlib.pyplot as plt

# Scatter plot dat
plt.scatter(X, y, color="blue", label="Data")

# Regresní přímka
plt.plot(X, model.predict(X), color="red", label="Regresní přímka")

plt.xlabel("Věk")
plt.ylabel("Plat")
plt.title("Lineární regrese: Věk vs Plat")
plt.legend()
plt.show()

# Přesnost modelu (R²)
print(f"Přesnost modelu (R²): {model.score(X, y):.2f}")

import joblib

# Uložení modelu do souboru
joblib.dump(model, "linear_model.pkl")
print("Model uložen jako linear_model.pkl")

