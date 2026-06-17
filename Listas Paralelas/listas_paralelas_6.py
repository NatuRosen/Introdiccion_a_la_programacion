codigo_maq = []
tipo_maq = []
cant_matenimiento = []
costo_mantenimiento = []
prom = 0

def ingresar_datos(codigo_maq, tipo_maq, cant_matenimiento, costo_mantenimiento):
    sigue = True
    while sigue == True:
        codigo = int(input("Ingrese el código de la máquina (0 para finalizar): "))
        if codigo == 0:
            sigue = False
        else:
            tipo = input("Ingrese el tipo de máquina: ")
            cantidad = int(input("Ingrese la cantidad de mantenimientos realizados: "))
            costo = float(input("Ingrese el costo total de mantenimiento: "))
            codigo_maq.append(codigo)
            tipo_maq.append(tipo)
            cant_matenimiento.append(cantidad)
            costo_mantenimiento.append(costo)

def mostrar_datos(codigo_maq, tipo_maq, cant_matenimiento, costo_mantenimiento):
    print("Datos de las máquinas:")
    for i in range(len(codigo_maq)):
        print(f"Código: {codigo_maq[i]}, Tipo: {tipo_maq[i]}, Cantidad de Mantenimientos: {cant_matenimiento[i]}, Costo Total de Mantenimiento: {costo_mantenimiento[i]:.2f}")
    
def mayor_costo(costo_mantenimiento, codigo_maq):
    max = 0
    maq_max = None
    for i in range(len(costo_mantenimiento)):
        if costo_mantenimiento[i] > max:
            max = costo_mantenimiento[i]
            maq_max = codigo_maq[i]
    print(f"La máquina con mayor costo de mantenimiento es la máquina {maq_max} con un costo de {max:.2f}")

def promedio_costo(costo_mantenimiento, prom):
    suma = 0
    for i in range(len(costo_mantenimiento)):
        suma += costo_mantenimiento[i]
    if len(costo_mantenimiento) == 0:
        print("No se ingresaron máquinas, no se pudo calcular el promedio.")
    else:
        prom = suma / len(costo_mantenimiento)
        print(f"Costo promedio de mantenimiento por máquina: {prom:.2f}")

def mayor_promedio(costo_mantenimiento, prom, codigo_maq):
    print("Máquinas con costo de mantenimiento por encima del promedio: ")
    for i in range(len(costo_mantenimiento)):
        if costo_mantenimiento[i] > prom:
            print(f" - Máquina {codigo_maq[i]} con un costo de {costo_mantenimiento[i]:.2f}")

def busqueda(codigo_maq, tipo_maq, cant_matenimiento, costo_mantenimiento):
    busq = int(input("Ingrese el código de la máquina a buscar: "))
    valid = False
    for i in range(len(codigo_maq)):
        if codigo_maq[i] == busq:
            print(f"Código: {codigo_maq[i]}, Tipo: {tipo_maq[i]}, Cantidad de Mantenimientos: {cant_matenimiento[i]}, Costo Total de Mantenimiento: {costo_mantenimiento[i]:.2f}")
            valid = True
    if valid == False:
        print(f"La máquina con código {busq} no se encuentra en la lista.")

ingresar_datos(codigo_maq, tipo_maq, cant_matenimiento, costo_mantenimiento)
mostrar_datos(codigo_maq, tipo_maq, cant_matenimiento, costo_mantenimiento)
mayor_costo(costo_mantenimiento, codigo_maq)
promedio_costo(costo_mantenimiento, prom)
mayor_promedio(costo_mantenimiento, prom, codigo_maq)
busqueda(codigo_maq, tipo_maq, cant_matenimiento, costo_mantenimiento)