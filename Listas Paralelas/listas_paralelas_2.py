camion = []
km_recorridos = []
km_totales = [0, 0, 0, 0, 0]
consumos = [10, 20, 30, 40, 50]
total_consumo = [0, 0, 0, 0, 0]
prom = None

def ingresar_datos():
    sigue = True
    while sigue == True:
        valido = False
        while valido == False:
            nro_camion = int(input("Ingrese el número de camión (1-5) (0 para terminar): "))
            if nro_camion == 0:
                sigue = False
                valido = True
                print("Ingreso de datos finalizado.")
            elif nro_camion >= 1 and nro_camion <= 5:
                camion.append(nro_camion)
                valido = True
            else:
                print("Número de camión inválido. Debe ser entre 1 y 5.")
        if sigue == True:
            km_valido = False
            while km_valido == False:
                km = int(input("Ingrese los kilómetros recorridos: "))
                if km > 0:
                    km_valido = True
                else:
                    print("Kilómetros inválidos. Debe ser un número positivo.")
            km_valido = False
            km_recorridos.append(km)

def km_por_camion(camion, km_recorridos, km_totales):
    for i in range(len(camion)):
        km_totales[camion[i]-1] += km_recorridos[i]
    print("Kilómetros totales por camión:")
    for i in range(len(km_totales)):
        print(f"Camión {i+1}: {km_totales[i]} km")

def consumo_por_camion(km_totales, consumos, total_consumo):
    for i in range(len(km_totales)):
        total_consumo[i] = km_totales[i] * consumos[i]
    print("Consumo total por camión:")
    for i in range(len(total_consumo)):
        print(f"Camión {i+1}: {total_consumo[i]} litros")

def mayor_consumo(total_consumo, camion):
    mas_consumo = []
    camion_mas_consumo = []
    max = 0
    camion_max = None
    for i in range(len(total_consumo)):
        if total_consumo[i] > max:
            max = total_consumo[i]
            camion_max = camion[i]
    mas_consumo.append(max)
    camion_mas_consumo.append(camion_max)
    for i in range(len(total_consumo)):
        if total_consumo[i] == max and camion[i] != camion_max:
            mas_consumo.append(total_consumo[i])
            camion_mas_consumo.append(camion[i])
    print("Camión(es) con mayor consumo: ")
    for i in range(len(camion_mas_consumo)):
        print(f" - {camion_mas_consumo[i]} con {mas_consumo[i]} litros")

def promedio_km(km_totales, prom):
    suma = 0
    for i in range(len(km_totales)):
        suma += km_totales[i]    
    prom = suma/len(km_totales)
    print(f"Promedio de kilómetros recorridos por camión: {prom} km")

def supera_promedio(km_totales, prom):
    print("Camiones que superan el promedio de kilómetros recorridos:")
    for i in range(len(km_totales)):
        if km_totales[i] > prom:
            print(f" - Camión {i+1} con {km_totales[i]} km")

ingresar_datos()
if len(camion) > 0:
    km_por_camion(camion, km_recorridos, km_totales)
    consumo_por_camion(km_totales, consumos, total_consumo)
    promedio_km(km_totales, prom)
    supera_promedio(km_totales, prom)