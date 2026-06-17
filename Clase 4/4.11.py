contador = 0
num = int(input("Ingrese un número: "))
for i in range(2,num):
    if num % i == 0:
        contador += 1
if contador == 0:
    print("El número es primo.")
else:
    print("El número no es primo.")