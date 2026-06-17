codigo_linea = []
nombre_sector = []
cantidad_operarios = []
unidades_producidas = []
horas_trabajadas = []
lista_eficiencias = []
prom = 0

def ingresar_datos(codigo_linea, nombre_sector, cantidad_operarios, unidades_producidas, horas_trabajadas):
    sigue = True
    while sigue == True:
        codigo = int(input("Ingrese el código de la línea de producción (0 para finalizar): "))
        if codigo == 0:
            sigue = False
        else:
            nombre = input("Ingrese el nombre del sector: ")
            operarios = int(input("Ingrese la cantidad de operarios: "))
            unidades = int(input("Ingrese la cantidad de unidades producidas: "))
            horas = int(input("Ingrese la cantidad de horas trabajadas: "))
            codigo_linea.append(codigo)
            nombre_sector.append(nombre)
            cantidad_operarios.append(operarios)
            unidades_producidas.append(unidades)
            horas_trabajadas.append(horas)

def mostrar_datos(codigo_linea, nombre_sector, cantidad_operarios, unidades_producidas, horas_trabajadas):
    print("Datos de las líneas de producción:")
    for i in range(len(codigo_linea)):
        print(f"Código: {codigo_linea[i]}, Sector: {nombre_sector[i]}, Operarios: {cantidad_operarios[i]}, Unidades Producidas: {unidades_producidas[i]}, Horas Trabajadas: {horas_trabajadas[i]}")

def mas_produccion(unidades_producidas, codigo_linea):
    max = 0
    linea_max = None
    for i in range(len(unidades_producidas)):
        if unidades_producidas[i] > max:
            max = unidades_producidas[i]
            linea_max = codigo_linea[i]
    print(f"Línea de producción con mayor cantidad de unidades producidas: Línea {linea_max} con {max} unidades")

def eficiencia_linea(unidades_producidas, horas_trabajadas, codigo_linea, lista_eficiencias):
    for i in range(len(unidades_producidas)):
        if horas_trabajadas[i] > 0:
            eficiencia = unidades_producidas[i] / horas_trabajadas[i]
            lista_eficiencias.append(eficiencia)
            print(f"Línea {codigo_linea[i]}: Eficiencia de {eficiencia:.2f} unidades/hora")
        else:
            print(f"Línea {codigo_linea[i]}: No se puede calcular la eficiencia.")

def prom_eficiencia(lista_eficiencias, prom):
    suma = 0
    for i in range(len(lista_eficiencias)):
        suma += lista_eficiencias[i]
    if len(lista_eficiencias) == 0:
        print("No se ingresaron líneas de producción, no se pudo calcular el promedio de eficiencia.")
    else:
        prom = suma / len(lista_eficiencias)
        print(f"Promedio de eficiencia de las líneas de producción: {prom:.2f} unidades/hora")

def mayor_promedio(lista_eficiencias, codigo_linea, prom):
    for i in range(len(lista_eficiencias)):
        if lista_eficiencias[i] > prom:
            print(f"Línea {codigo_linea[i]} con eficiencia de {lista_eficiencias[i]:.2f} unidades/hora está por encima del promedio.")

def promedio_operarios(cantidad_operarios, prom):
    suma = 0
    for i in range(len(cantidad_operarios)):
        suma += cantidad_operarios[i]
    if len(cantidad_operarios) == 0:
        print("No se ingresaron líneas de producción, no se pudo calcular el promedio de operarios.")
    else:
        prom = suma / len(cantidad_operarios)
        print(f"Promedio de operarios por línea de producción: {prom:.2f} operarios")

def busqueda(codigo_linea, nombre_sector, cantidad_operarios, unidades_producidas, horas_trabajadas):
    busq = int(input("Ingrese el código de la línea de producción a buscar: "))
    valid = False
    for i in range(len(codigo_linea)):
        if codigo_linea[i] == busq:
            print(f"Código: {codigo_linea[i]}, Sector: {nombre_sector[i]}, Operarios: {cantidad_operarios[i]}, Unidades Producidas: {unidades_producidas[i]}, Horas Trabajadas: {horas_trabajadas[i]}")
            valid = True
    if valid == False:
        print(f"La línea de producción con código {busq} no se encuentra en la lista.")