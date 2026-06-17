sigue = True
valido = False
suma = 0
cant = 0
estado = None
while sigue == True:
    lote = int(input("Ingrese el número de lote (Menor a 0 para cortar): "))
    if lote < 0:
        sigue = False
    else:
        while valido == False:
            met1 = int(input("Ingrese la primera métrica del lote: "))
            met2 = int(input("Ingrese la segunda métrica del lote: "))
            if met1 < 0 or met2 < 0 or met1 > 10 or met2 > 10:
                print("Las métricas deben estar entre 0 y 10. Intente nuevamente.")
            elif met1 >= 7 and met2 >= 7:
                estado = "APROBADO"
                suma += met1 + met2
                cant += 2
                valido = True
            elif met1 >= 4 and met2 >= 4:
                estado = "REPROCESO NECESARIO"
                valido = True
            else:
                estado = "RECHAZADO"
                valido = True
    if estado != None:
        print("El lote ", lote, "obtuvo las métricas: ", met1, " y ", met2, " y su estado es: ", estado)
    estado = None
    valido = False

print(suma)
print(cant)

if cant > 0:
    print("El promedio de las métricas de los lotes aprobados es: ", suma/cant)