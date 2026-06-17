valido = True
precio = 10
suma = 0
contador = 0
while valido == True:
    consumo = int(input("Ingrese el consumo de energía (negativo o cero para terminar): "))
    if consumo > 0:
        if consumo < 50:
           precio *= 0.965
           suma += precio
           contador += 1
           print("El precio a pagar es: ", precio)
        elif consumo >= 50 and consumo <= 150:
            precio *= 1.1
            suma += precio
            contador += 1
            print("El precio a pagar es: ", precio)
        elif consumo >= 151 and consumo <= 300:
            precio *= 1.2
            suma += precio
            contador += 1
            print("El precio a pagar es: ", precio)
        else:
            precio *= 1.25
            suma += precio
            contador += 1
            print("El precio a pagar es: ", precio)
    else:
        valido = False

if contador > 0:
    print("El precio promedio a pagar es: ", suma/contador)
else:
    print("No se ingresaron consumos válidos.")