regular = int(input("Ingrese la cantidad de asientos regulares vendidos: "))
ejecutivo = int(input("Ingrese la cantidad de asientos ejecutivos vendidos: "))
total = regular * 12000 + ejecutivo * 120000 * 1.3
print("El total recaudado es: ", total)