max_1 = None
max_2 = None
presion = None
while presion != 0:
    presion = int(input("Ingrese la lectura del pico de presión (o 0 para finalizar): "))
    if presion != 0:
        if max_1 is None or presion > max_1:
            max_2 = max_1
            max_1 = presion
        elif max_2 is None or presion > max_2:
            max_2 = presion
if max_1 != None:
    print(f"La mayor lectura de presión fue: {max_1}")
    if max_2 != None:
        print(f"La segunda mayor lectura de presión fue: {max_2}")
    else:
        print("No se ingresaron suficientes lecturas de presión.")
else:
    print("No se ingresaron lecturas de presión.")