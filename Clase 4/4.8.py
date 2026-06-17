sum = 0
contador = 0
while sum < 100:
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        sum += num
    contador += 1
print("La suma de los números pares ingresados es: ", sum)
print("La cantidad de números ingresados es: ", contador)