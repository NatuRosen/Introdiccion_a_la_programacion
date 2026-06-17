codigos_prod = []
tipos_prod = []
pesos_optimos = []
pesos_medidos = []

def ingresar_cantidad_productos():
    valid = False
    while valid == False:
        cantidad = int(input("Ingrese la cantidad de productos que desee ingresar: "))
        if cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
        else:
            valid = True
    return cantidad

def ingreso_productos (codigos_prod, tipos_prod, pesos_optimos, cantidad):
    for i in range(cantidad):
        cod_valido = False
        tipo_valido = False
        peso_valido = False
        while cod_valido == False:
            codigo = int(input(f"Ingrese el código del producto {i+1}: "))
            if codigo >= 0:
                cod_valido = True
            else:
                print("El código debe ser mayor o igual a 0.")
        while tipo_valido == False:
            tipo = input(f"Ingrese el tipo del producto {i+1} (A / B): ")
            print(tipo)
            if tipo == 'A' or tipo == 'B' or tipo == 'a' or tipo == 'b':
                tipo_valido = True
            else:
                print("El tipo de de producto debe ser A o B.")
        while peso_valido == False:
            peso_ideal = int(input(f"Ingrese el peso ideal del producto {i+1}: "))
            if peso_ideal > 0:
                peso_valido = True
            else:
                print("El peso ideal debe ser mayor a 0.")
        codigos_prod.append(codigo)
        tipos_prod.append(tipo)
        pesos_optimos.append(peso_ideal)

def mostrar_datos(codigos_prod, tipos_prod, pesos_optimos, pesos_medidos):
    for i in range(len(codigos_prod)):
        print(f"Producto {i+1}:")
        print(f"Código: {codigos_prod[i]}. Tipo: {tipos_prod[i]}. Peso Óptimo: {pesos_optimos[i]}. Peso medido: {pesos_medidos[i]}")

def control_lotes(codigos_prod, pesos_optimos, pesos_medidos):
    sigue = True
    contador = 0
    no_validos = 0
    while sigue == True:
        busq = int(input("Ingrese el producto al cual cargarle la medición: "))
        if busq <= 0:
            sigue = False
        else:
            codigo_encontrado = False
            continuar = False
            while codigo_encontrado == False:
                encontrado = False
                for i in range(len(codigos_prod)):
                    if busq == codigos_prod[i]:
                        encontrado = True
                        indice = i
                if encontrado == False:
                    print("No se encontró ningún producto con el código buscado")
                    codigo_encontrado = True
                else:
                    codigo_encontrado = True
                    continuar = True
            if continuar == True:
                contador += 1
                medicion_valida = False
                while medicion_valida == False:
                    peso = int(input(f"Ingrese el peso medido para el producto {busq}: "))
                    if peso <= 0:
                        print("El peso debe ser mayor a 0.")
                    else:
                        medicion_valida = True
                if peso > pesos_optimos[indice]:
                    print("El producto fue rechazado. El peso medido supera al óptimo.")
                    no_validos += 1
                else:
                    pesos_medidos[indice] = peso
    if contador != 0:
        print(f"Se rechazaron {no_validos} de {contador} productos medidos.")
    else:
        print("No se realizaron búsquedas.")

def mayores_mediciones(codigos_prod, pesos_medidos):
    mayor_peso = 0
    cod_mayor_peso = None
    for i in range(len(codigos_prod)):
        if pesos_medidos[i] > mayor_peso:
            mayor_peso = pesos_medidos[i]
            cod_mayor_peso = codigos_prod[i]
    if mayor_peso == 0:
        print("No hay peso máximo. No se registraron mediciones.")
    else:
        print(f"El producto con mayor peso medido fue el {cod_mayor_peso}, pesando {mayor_peso}")

def prom_pesos_optmos(pesos_optimos):
    suma = 0
    for i in range(len(pesos_optimos)):
        suma += pesos_optimos[i]
    if len(pesos_optimos) != 0:
        prom = suma / len(pesos_optimos)
        print(f"El promedio de los pesos óptimos medidos es: {prom:.2f}")
    else:
        print("No se puede calcular el promedio. La cantidad de pesos óptimos registrada es 0.")

cantidad = ingresar_cantidad_productos()
for i in range(cantidad):
    pesos_medidos.append(0)
ingreso_productos (codigos_prod, tipos_prod, pesos_optimos, cantidad)
control_lotes(codigos_prod, pesos_optimos, pesos_medidos)
mostrar_datos(codigos_prod, tipos_prod, pesos_optimos, pesos_medidos)
mayores_mediciones(codigos_prod, pesos_medidos)
prom_pesos_optmos(pesos_optimos)