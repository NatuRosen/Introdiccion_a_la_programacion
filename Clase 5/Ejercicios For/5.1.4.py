valido = False
valido2 = False
suma = 0
while valido == False:
    horas = int(input("Ingrese la cantidad de horas trabajadas del turno: "))
    if horas >= 0:
        valido = True
    else:
        print("La cantidad de horas no puede ser negativa. Intente nuevamente.")
for i in range(horas):
    while valido2 == False:
        produccion = int(input("Ingrese la produccion del turno: "))
        if produccion >= 0:
            suma += produccion
            valido2 = True
        else:
            print("La produccion no puede ser negativa. Intente nuevamente.")
print("La produccion total del turno es: ", suma)