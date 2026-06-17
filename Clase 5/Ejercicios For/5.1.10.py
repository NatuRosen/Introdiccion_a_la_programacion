valid = False
terna = 0
cant_ternas = 0
caida = 0
cant_caidas = 0
for i in range(18):
    while valid == False:
        medida = int(input("Ingrese la medición de tensión: "))
        if medida != 0:
            valid = True
        else:
            print("La medición no puede ser cero. Intente nuevamente.")
    if medida > 0:
        if caida > 0:
            caida = 0
        terna += 1
    elif medida < 0:
        if terna > 0:
            terna = 0
        caida += 1
    if terna == 3:
        cant_ternas += 1
        terna = 0
    if caida == 3:
        cant_caidas += 1
        caida = 0
    valid = False
print("La cantidad de ternas es: ", cant_ternas)
print("La cantidad de caídas es: ", cant_caidas)