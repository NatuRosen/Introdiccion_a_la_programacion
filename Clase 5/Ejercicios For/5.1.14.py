primero = 0
segundo = 0
tercero = 0
cuarto = 0
origen = 0
for i in range(15):
    x = int(input(f"Ingrese la coordenada x del punto {i+1}: "))
    y = int(input(f"Ingrese la coordenada y del punto {i+1}: "))
    if x > 0 and y > 0:
        primero += 1
    elif x < 0 and y > 0:
        segundo += 1
    elif x < 0 and y < 0:
        tercero += 1
    elif x > 0 and y < 0:
        cuarto += 1
    elif x == 0 and y == 0:
        origen += 1
print("La cantidad de puntos en el primer cuadrante es: ", primero)
print("La cantidad de puntos en el segundo cuadrante es: ", segundo)
print("La cantidad de puntos en el tercer cuadrante es: ", tercero)
print("La cantidad de puntos en el cuarto cuadrante es: ", cuarto)
print("La cantidad de puntos en el origen es: ", origen)