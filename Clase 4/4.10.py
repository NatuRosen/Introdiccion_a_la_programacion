num = int(input("Ingrese un número entero mayor a 0: "))
if num > 0:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("El factorial de", num, "es:", factorial)
else:
    print("El número ingresado no es mayor a 0.")