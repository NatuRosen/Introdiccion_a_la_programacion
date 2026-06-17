suma_x = 0
for i in range(6):
    valido_x = False
    valido_y = False
    valido_z = False
    mas_alta = None
    eje_mas_alta = None
    mult_7 = 0
    while valido_x == False:
        eje_x = int(input(f"Ingrese la vibración del eje X para el sensor {i+1}: "))
        if eje_x >= 0:
            valido_x = True
        else:
            print("Vibración inválida. Vuelva a ingresarla.")
    mas_alta = eje_x
    eje_mas_alta = "X"
    if eje_x % 7 == 0:
        mult_7 += 1
    suma_x += eje_x
    while valido_y == False:
        eje_y = int(input(f"Ingrese la vibración del eje Y para el sensor {i+1}: "))
        if eje_y >= 0:
            valido_y = True
        else:
            print("Vibración inválida. Vuelva a ingresarla.")
    if eje_y > mas_alta:
        mas_alta = eje_y
        eje_mas_alta = "Y"
    if eje_y % 7 == 0:
        mult_7 += 1
    while valido_z == False:
        eje_z = int(input(f"Ingrese la vibración del eje Z para el sensor {i+1}: "))
        if eje_z >= 0:
            valido_z = True
        else:
            print("Vibración inválida. Vuelva a ingresarla.")
    if eje_z > mas_alta:
        mas_alta = eje_z
        eje_mas_alta = "Z"
    if eje_z % 7 == 0:
        mult_7 += 1
    print(f"La vibración más alta para el sensor {i+1} es: {mas_alta}, en el eje {eje_mas_alta}")
    print(f"De la terna {i+1}, {mult_7} superaron el umbral de seguridad (múltiplos de 7).")
print(f"El promedio de las vibraciones del eje X es: {suma_x/6:.2f}")