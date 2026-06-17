valido = False
suma_pos = 0
suma_neg = 0
suma_cero = 0
while valido == False:
    lote = int(input("Ingrese el tamaño del lote (0 - 12): "))
    if 0 < lote <= 12:
        valido = True
    elif lote < 0:
        print("Cantidad inválida.")
    else:
        print("Capacidad de lote excedida.")
for i in range(lote):
    desv = int(input("Ingrese la desviación del lote: "))
    if desv > 0:
        suma_pos += desv
    elif desv < 0:
        suma_neg += desv
    else: 
        suma_cero += 1
print("El promedio de las desviaciones positivas es: ", suma_pos/lote)
print("El promedio de las desviaciones negativas es: ", suma_neg/lote)
print("La cantidad de piezas perfectas es: ", suma_cero)