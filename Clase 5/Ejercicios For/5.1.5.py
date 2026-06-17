valido = False
valido2 = False
suma_10 = 0
cant_50 = 0
suma_par = 0
while valido == False:
    lecturas = int(input("Ingrese el valor de lecturas: "))
    if lecturas >= 0:
        valido = True
    else:
        print("La cantidad de lecturas no puede ser negativa. Intente nuevamente.")
for i in range(lecturas):
    while valido2 == False:
        medicion = int(input(f"Ingrese la lectura {i+1} de presión hidráulica: "))
        if medicion >= 0:
            if medicion % 10 == 0:
                suma_10 += medicion
            if lecturas > 50:
                cant_50 += 1
            valido2 = True
        else:
            print("La produccion no puede ser negativa. Intente nuevamente.")
    if (i+1) % 2 == 0:
        suma_par += medicion
print("La suma de las lecturas que son múltiplos de 10 es: ", suma_10)
print("La cantidad de lecturas ingresadas es mayor a 50 es: ", cant_50)
print("La suma de las lecturas que son pares es: ", suma_par)