menor = None
mayor = None
num = None
while num != -1:
    num = int(input("Ingrese un número (o -1 para terminar): "))
    if num != -1:
        if menor is None or num < menor:
            menor = num
        if mayor is None or num > mayor:
            mayor = num
print("El menor número ingresado fue: ", menor)
print("El mayor número ingresado fue: ", mayor)