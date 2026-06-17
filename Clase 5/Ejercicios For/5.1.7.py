kg_valido = False
cm_valido = False
suma_kg = 0
suma_cm = 0
pesadas = 0
cortas = 0
for i in range(45):
    while kg_valido == False:
        kg = int(input("Ingrese el peso en kg: "))
        if kg >= 0:
            kg_valido = True
            suma_kg += kg
            if kg >= 50:
                pesadas += 1
        else:
            print("El peso no puede ser negativo. Intente nuevamente.")
    while cm_valido == False:
        cm = int(input("Ingrese la altura en cm: "))
        if cm >= 0:
            cm_valido = True
            suma_cm += cm
            if cm < 120:
                cortas += 1
        else:
            print("La longitud no puede ser negativa. Intente nuevamente.")
print("El peso promedio de las personas es: ", suma_kg/45)
print("La altura promedio de las personas es: ", suma_cm/45)
print("La cantidad de personas que pesan 50 kg o más es: ", pesadas)
print("La cantidad de vigas que miden menos de 120 cm es: ", cortas)