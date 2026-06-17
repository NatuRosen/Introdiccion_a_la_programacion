codigo_material = []
descripcion_material = []
stock_actual = []
stock_minimo = []
costo_unitario = []
prom = 0

def cargar_materiales(codigo_material, descripcion_material, stock_actual, stock_minimo, costo_unitario):
    sigue = True
    while sigue == True:
        codigo = int(input("Ingrese el código del material (0 para finalizar): "))
        if codigo == 0:
            sigue = False
        else:
            descripcion = input("Ingrese la descripción del material: ")
            stock_act = int(input("Ingrese el stock actual del material: "))
            stock_min = int(input("Ingrese el stock mínimo del material: "))
            costo_unit = float(input("Ingrese el costo unitario del material: "))
            codigo_material.append(codigo)
            descripcion_material.append(descripcion)
            stock_actual.append(stock_act)
            stock_minimo.append(stock_min)
            costo_unitario.append(costo_unit)

def mostrar_materiales(codigo_material, descripcion_material, stock_actual, stock_minimo, costo_unitario):
    print("Materiales cargados:")
    for i in range(len(codigo_material)):
        print(f"Código: {codigo_material[i]}, Descripción: {descripcion_material[i]}, Stock Actual: {stock_actual[i]}, Stock Mínimo: {stock_minimo[i]}, Costo Unitario: {costo_unitario[i]}")

def materiales_bajo_stock(codigo_material, stock_actual, stock_minimo):
    print("Materiales con stock por debajo del mínimo:")
    for i in range(len(codigo_material)):
        if stock_actual[i] < stock_minimo[i]:
            print(f" - Código: {codigo_material[i]}, Stock Actual: {stock_actual[i]}, Stock Mínimo: {stock_minimo[i]}")

def valor_total_stock(codigo_material, stock_actual, costo_unitario):
    suma = 0
    for i in range(len(stock_actual)):
        valor_total = stock_actual[i] * costo_unitario[i]
        suma += valor_total
        print(f"Valor total del stock del material {codigo_material[i]}: {valor_total:.2f}")
    print(f"Valor total del inventario: {suma:.2f}")

def costo_unitario_promedio(costo_unitario, prom):
    suma = 0
    for i in range(len(costo_unitario)):
        suma += costo_unitario[i]
    if len(costo_unitario) == 0:
        print("No se ingresaron materiales, no se pudo calcular el costo unitario promedio.")
    else:
        prom = suma / len(costo_unitario)
        print(f"Costo unitario promedio: {prom:.2f}")

def busqueda(codigo_material, descripcion_material, stock_actual, stock_minimo, costo_unitario):
    busq = int(input("Ingrese el código del material a buscar: "))
    contador = 0
    for i in range(len(codigo_material)):
        if codigo_material[i] == busq:
            contador += 1
            print(f"Código: {codigo_material[i]}, Descripción: {descripcion_material[i]}, Stock Actual: {stock_actual[i]}, Stock Mínimo: {stock_minimo[i]}, Costo Unitario: {costo_unitario[i]}")
    if contador == 0:
        print(f"El material con código {busq} no se encuentra en la lista.")

cargar_materiales(codigo_material, descripcion_material, stock_actual, stock_minimo, costo_unitario)
mostrar_materiales(codigo_material, descripcion_material, stock_actual, stock_minimo, costo_unitario)
materiales_bajo_stock(codigo_material, stock_actual, stock_minimo)
valor_total_stock(codigo_material, stock_actual, costo_unitario)
costo_unitario_promedio(costo_unitario, prom)
busqueda(codigo_material, descripcion_material, stock_actual, stock_minimo, costo_unitario)