suma = 0
cant = 0
for i in range(50):
    num = int(input("Ingrese un numero: "))
    if num > 100:
        suma += num
        cant += 1
if cant > 0:
    print("El promedio de las temperaturas mayores a 100 es: ", suma/cant)
else:
    print("No se ingresaron temperaturas mayores a 100")