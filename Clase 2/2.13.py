num = input("Ingrese un número entero positivo de 4 dígitos: ")
suma = 0
while len(num) > 1:
    for i in range(len(num)):
        suma += int(num[i])
    num = str(suma)
    suma = 0
print("La suma de los dígitos es: ", num)