nro_maquina = []
sector = []
piezas_producidas = []
cantidad_horas = []
promedio = None
sigue = True
sigue2 = True

def ingresar_datos(maq, sec, piezas, horas, sigue):
    valid = False
    while sigue == True:
        while valid == False:
            maquina = int(input("Ingrese el número de máquina de 3 cifras: "))
            if maquina >= 100 and maquina <= 999:
                valid = True
                maq.append(maquina)
            elif maquina == 0:
                print("Ingreso de datos finalizado.")
                valid = True
                sigue = False
            else:
                print("Número de máquina inválido. Debe ser de 3 cifras.")
        
        if sigue == True:
            sec.append(input("Ingrese el sector: "))
            piezas.append(int(input("Ingrese la cantidad de piezas producidas: ")))
            horas.append(int(input("Ingrese la cantidad de horas trabajadas: ")))
            valid = False

def mostrar(maq, sec, piezas, horas):
    print("Nro Máquina\tSector\tPiezas Producidas\tHoras Trabajadas")
    for i in range(len(maq)):
        print(f"{maq[i]}\t{sec[i]}\t{piezas[i]}\t{horas[i]}")

def mayor_produccion(piezas, maq):
    mas_piezas = []
    maq_mas_piezas = []
    max = 0
    maq_max = None
    for i in range(len(piezas)):
        if piezas[i] > max:
            max = piezas[i]
            maq_max = maq[i]
    mas_piezas.append(max)
    maq_mas_piezas.append(maq_max)
    for i in range(len(piezas)):
        if piezas[i] == max and maq[i] != maq_max:
            mas_piezas.append(piezas[i])
            maq_mas_piezas.append(maq[i])
    print("Máquina(s) con mayor producción: ")
    for i in range(len(maq_mas_piezas)):
        print(f" - {maq_mas_piezas[i]} con {mas_piezas[i]} piezas")

def prom_piezas(piezas, prom):
    suma = 0
    for i in range(len(piezas)):
        suma += piezas[i]
    if len(piezas) == 0:
        print("No se ingresaron maquinas, no se pudo calcular el promedio.")
    else:
        prom = suma / len(piezas)
        print(f"Promedio de piezas producidas: {prom:.2f}")
    return prom

def debajo_promedio(piezas, prom, maq):
    print("Máquinas con producción por debajo del promedio: ")
    for i in range(len(piezas)):
        if piezas[i] < prom:
            print(f" - {maq[i]} con {piezas[i]} piezas")

def productividad(piezas, horas, maq):
    for i in range(len(piezas)):
        if horas[i] > 0:
            prod = piezas[i] / horas[i]
            print(f"Productividad de la máquina {maq[i]}: {prod:.2f} piezas/hora")
        else:
            print(f"La máquina {maq[i]} no trabajó horas, no se puede calcular productividad.")

def busqueda(maq, piezas, sigue):
    busq = int(input("Ingrese el número de máquina a buscar: "))
    valid = False
    if sigue == True:
        if busq == 0:
            sigue = False
        else:    
            for i in range(len(maq)):
                if maq[i] == busq:
                    print(f"La máquina {busq} produjo {piezas[i]} piezas.")
                    valid = True
            if valid == False:
                print(f"La máquina {busq} no se encuentra en la lista.")
    return sigue


ingresar_datos(nro_maquina, sector, piezas_producidas, cantidad_horas, sigue)
if len(piezas_producidas) > 0:
    mostrar(nro_maquina, sector, piezas_producidas, cantidad_horas)
    mayor_produccion(piezas_producidas, nro_maquina)
    promedio = prom_piezas(piezas_producidas, promedio)
    debajo_promedio(piezas_producidas, promedio, nro_maquina)
    productividad(piezas_producidas, cantidad_horas, nro_maquina)
    while sigue2 == True:
        sigue2 = busqueda(nro_maquina, piezas_producidas, sigue2)
else:
    print("No se ingresaron máquinas, no se pueden mostrar resultados.")