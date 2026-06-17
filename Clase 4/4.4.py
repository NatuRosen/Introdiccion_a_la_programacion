num = None
contador = 0
while num != -1:
    num = int(input("Ingrese un número (o -1 para terminar): "))
    if contador == 0:
        primero = num
    contador += 1
    if num != -1:
        ultimo = num
print("El primer número ingresado fue: ", primero)
print("El último número ingresado fue: ", ultimo)