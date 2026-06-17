num = None
contador = 0
while num != -1:
    num = int(input("Ingrese un número (o -1 para terminar): "))
    if num != -1:
        contador += 1
if contador > 0:
    if contador % 2 == 0:
        print("La cantidad de números ingresados es par.")
    else:
        print("La cantidad de números ingresados es impar.")
else:
    print("No se ingresaron números.")