import random

numeros = []

for i in range(0, 6):
    numero = random.randint(1, 60)
    if numero in numeros:
        while numero in numeros:
            numero = random.randint(1, 60)
    numeros.append(numero)

numeros.sort()
print(numeros)
