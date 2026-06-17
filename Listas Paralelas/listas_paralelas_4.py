legajos = []
nombres = []
cantidad_horas = []
cantidad_piezas = []

def ingresar_datos(legajos, nombres, cantidad_horas, cantidad_piezas):
    sigue = True
    while sigue == True:
        legajo = int(input("Ingrese el legajo del operario (0 para finalizar): "))
        if legajo == 0:
            sigue = False
        else:
            nombre = input("Ingrese el nombre del operario: ")
            horas = int(input("Ingrese la cantidad de horas trabajadas: "))
            piezas = int(input("Ingrese la cantidad de piezas fabricadas: "))
            legajos.append(legajo)
            nombres.append(nombre)
            cantidad_horas.append(horas)
            cantidad_piezas.append(piezas)

def mostrar_datos(legajos, nombres, cantidad_horas, cantidad_piezas):
    print("Datos de los operarios:")
    for i in range(len(legajos)):
        print(f"Legajo: {legajos[i]}, Nombre: {nombres[i]}, Horas Trabajadas: {cantidad_horas[i]}, Piezas Fabricadas: {cantidad_piezas[i]}")

def rendimiento(legajos, nombres, cantidad_horas, cantidad_piezas):
    print("Rendimiento de los operarios:")
    for i in range(len(legajos)):
        if cantidad_horas[i] > 0 and cantidad_piezas[i] > 0:
            rendimiento = cantidad_piezas[i] / cantidad_horas[i]
            print(f"Legajo: {legajos[i]}, Nombre: {nombres[i]}, Rendimiento: {rendimiento:.2f} piezas/hora")
        else:
            print(f"Legajo: {legajos[i]}, Nombre: {nombres[i]}, Rendimiento: No se puede calcular.")

ingresar_datos(legajos, nombres, cantidad_horas, cantidad_piezas)
mostrar_datos(legajos, nombres, cantidad_horas, cantidad_piezas)
rendimiento(legajos, nombres, cantidad_horas, cantidad_piezas)