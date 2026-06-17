num = int(input("Ingrese un número de 3 dígitos: "))
centenas = num // 100
decenas = (num % 100) // 10
unidades = num % 10
print("La cantidad de centenas es: ", centenas)
print("La cantidad de decenas es: ", decenas)
print("La cantidad de unidades es: ", unidades)