nro_lote = []
cantidad = []
cantidad_defectuosa = []

def ingresar_datos(nro_lote, cantidad, cantidad_defectuosa):
    sigue = True
    while sigue == True:
        lote = int(input("Ingrese el número de lote (0 para finalizar): "))
        if lote == 0:
            sigue = False
        else:
            cant = int(input("Ingrese la cantidad producida en el lote: "))
            cant_defectuosa = int(input("Ingrese la cantidad defectuosa en el lote: "))
            nro_lote.append(lote)
            cantidad.append(cant)
            cantidad_defectuosa.append(cant_defectuosa)

def produccion_total(cantidad):
    suma = 0
    for i in range(len(cantidad)):
        suma += cantidad[i]
    print(f"Cantidad total producida: {suma} unidades")

def total_defectuosa(cantidad_defectuosa):
    suma = 0
    for i in range(len(cantidad_defectuosa)):
        suma += cantidad_defectuosa[i]
    print(f"Cantidad total defectuosa: {suma} unidades")

def porc_desperdicio(cantidad, cantidad_defectuosa):
    defectuosas = 0
    producidas = 0
    for i in range(len(cantidad)):
        producidas += cantidad[i]
    for i in range(len(cantidad_defectuosa)):
        defectuosas += cantidad_defectuosa[i]
    if producidas == 0:
        print("No se ingresaron lotes, no se pudo calcular el porcentaje de desperdicio.")
    else:
        porcentaje = (defectuosas / producidas) * 100
        print(f"Porcentaje de desperdicio: {porcentaje:.2f}%")

def lote_mas_desperdicio(nro_lote, cantidad, cantidad_defectuosa):
    for i in range(len(cantidad)):
        if cantidad[i] > 0:
            desperdicio = (cantidad_defectuosa[i] / cantidad[i]) * 100
            print(f"Lote {nro_lote[i]}: {desperdicio:.2f}% de desperdicio")
        else:
            print(f"Lote {nro_lote[i]} no produjo unidades, no se puede calcular el porcentaje de desperdicio.")

def prom_por_lote(cantidad, cantidad_defectuosa):
    for i in range(len(cantidad)):
        if cantidad[i] > 0:
            promedio = (cantidad[i] * 100) / (cantidad_defectuosa[i] + cantidad[i])
            print(f"Lote {nro_lote[i]}: Promedio de desperdicio por lote: {promedio:.2f}%")
        else:
            print(f"Lote {nro_lote[i]} no produjo unidades, no se puede calcular el promedio de desperdicio por lote.")