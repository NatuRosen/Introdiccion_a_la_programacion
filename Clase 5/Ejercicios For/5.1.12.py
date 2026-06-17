print("Números primos: ")
primos = 0
for i in range(2,101):
    contador = 0
    for j in range(2,i):
        if i % j == 0:
            contador += 1
    if contador == 0:
        primos += 1
        print(i)
print("Cantidad de números primos entre 1 y 100: ", primos)