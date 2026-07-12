
import pandas as pd

# Načtení CSV souboru se středníkem jako oddělovačem
df = pd.read_csv("data.csv", sep=";")

print("Prvních 5 řádků:")
print(df.head())

print("\nSloupce:")
print(df.columns)

print("\nVěk všech osob:")
print(df["age"])


# Průměrný věk
print("\nPrůměrný věk:")
print(df["age"].mean())

# Seřazení podle věku (od nejmladšího)
print("\nSeřazení podle věku:")
print(df.sort_values(by="age"))

# Přidání nového sloupce (např. věk za 5 let)
df["age_plus_5"] = df["age"] + 5
print("\nData s novým sloupcem:")
print(df)


import matplotlib.pyplot as plt

# Histogram věku
plt.hist(df["age"], bins=5, color="orange")
plt.title("Histogram věku")
plt.xlabel("Věk")
plt.ylabel("Počet")
plt.show()
