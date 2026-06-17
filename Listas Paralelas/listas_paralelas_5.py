nro_pedidos = []
codigo_productos = []
cantidades = []
tiempo_fabricacion = []
prom = 0

def ingresar_datos(nro_pedidos, codigo_productos, cantidades, tiempo_fabricacion):
    sigue = True
    while sigue == True:
        nro_pedido = int(input("Ingrese el número de pedido (0 para finalizar): "))
        if nro_pedido == 0:
            sigue = False
        else:
            codigo_producto = int(input("Ingrese el código del producto: "))
            cantidad = int(input("Ingrese la cantidad solicitada: "))
            tiempo = int(input("Ingrese el tiempo de fabricación en horas: "))
            nro_pedidos.append(nro_pedido)
            codigo_productos.append(codigo_producto)
            cantidades.append(cantidad)
            tiempo_fabricacion.append(tiempo)

def cant_pedidos(nro_pedidos):
    print(f"Cantidad total de pedidos ingresados: {len(nro_pedidos)}")

def unidades_por_producto(codigo_productos, cantidades):
    for i in range(len(codigo_productos)):
        suma = 0
        for j in range(len(codigo_productos)):
            if codigo_productos[i] == codigo_productos[j]:
                suma += cantidades[j]
        print(f"Producto {codigo_productos[i]}: {suma} unidades solicitadas")

def tiempo_total_fabricacion(tiempo_fabricacion):
    suma = 0
    for i in range(len(tiempo_fabricacion)):
        suma += tiempo_fabricacion[i]
    print(f"Tiempo total de fabricación para todos los pedidos: {suma} horas")

def pedido_mas_cantidad(nro_pedidos, cantidades):
    max = 0
    pedido_max = None
    for i in range(len(cantidades)):
        if cantidades[i] > max:
            max = cantidades[i]
            pedido_max = nro_pedidos[i]
    print(f"Pedido con mayor cantidad solicitada: Pedido {pedido_max} con {max} unidades")

def promedio_cantidad(cantidades, prom):
    for i in range(len(cantidades)):
        prom += cantidades[i]
    if len(cantidades) == 0:
        print("No se ingresaron pedidos, no se pudo calcular el promedio.")
    else:
        prom = prom / len(cantidades)
        print(f"Promedio de cantidad solicitada por pedido: {prom:.2f} unidades")

def mayor_promedio(cantidades, prom, nro_pedidos):
    print("Pedidos con cantidad solicitada por encima del promedio: ")
    for i in range(len(cantidades)):
        if cantidades[i] > prom:
            print(f" - Pedido {nro_pedidos[i]} con {cantidades[i]} unidades")

ingresar_datos(nro_pedidos, codigo_productos, cantidades, tiempo_fabricacion)
cant_pedidos(nro_pedidos)
unidades_por_producto(codigo_productos, cantidades)
tiempo_total_fabricacion(tiempo_fabricacion)
pedido_mas_cantidad(nro_pedidos, cantidades)
promedio_cantidad(cantidades, prom)
mayor_promedio(cantidades, prom, nro_pedidos)