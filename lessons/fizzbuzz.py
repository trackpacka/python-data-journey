FB="FizzBuzz"
F="Fizz"
B="Buzz"
vysledek=[]
for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        vysledek.append(FB)
    elif i % 3 == 0:
        vysledek.append(F)
    elif i % 5 == 0:
        vysledek.append(B)
    else:
        vysledek.append(i)
print(vysledek)
