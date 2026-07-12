hmotnost = float(input("zadej svou hmotnost v kg: "))
vyska = float(input("zadej svou výšku v metrech: "))

bmi= hmotnost / (vyska ** 2)

print(f"Tvoje BMI je {bmi:.1f}")