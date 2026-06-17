km = int(input("Ingrese la distancia en kilómetros: "))
min = 2700
if km > 0 and km <= 10:
    costo = km * 400
    if costo < min:
        costo = min
    print("El costo del viaje es: ", costo)
elif km > 10:
    costo = km * 200
    if costo < min:
        costo = min
    print("El costo del viaje es: ", costo)
else:
    print("Distancia no válida.")