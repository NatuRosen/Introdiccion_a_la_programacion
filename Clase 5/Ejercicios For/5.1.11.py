valid = False
factorial = 1
while valid == False:
    num = int(input("Ingrese un número mayor a 0: "))
    if num > 0:
        valid = True
    else:
        print("El número debe ser mayor a 0. Intente nuevamente.")
for i in range(num,0,-1):
    factorial *= i
print("El factorial de ", num, " es: ", factorial)