mayor = None
mayor_pos = None
suma = 0
for i in range(10):
    num = int(input("Ingrese un número: "))
    if mayor is None or num > mayor:
        mayor = num
        mayor_pos = i + 1
    suma += num
prom = suma / 10
print("El promedio de los números ingresados es: ", prom)
print("El mayor número ingresado fue: ", mayor)
print("El mayor número se ingresó en la posición: ", mayor_pos)