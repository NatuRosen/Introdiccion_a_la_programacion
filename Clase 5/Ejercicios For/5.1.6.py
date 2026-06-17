legajo = False
horas = False
sin_extra = 0
for i in range(20):
    while legajo == False:
        num = int(input("Ingrese el legajo del trabajador: "))
        if num >= 0 and num <= 9999:
            legajo = True
        else:
            print("El legajo debe ser un número entre 0 y 9999. Intente nuevamente.")
    while horas == False:
        extras = int(input("Ingrese la cantidad de horas extras trabajadas: "))
        if extras > 15:
            print("El trabajador con legajo ", num, "requiere descanso obligatorio.")
            horas = True
        elif extras == 0:
            sin_extra += 1
            horas = True
        elif extras > 0 and extras <= 15:
            horas = True
        else:
            print("La cantidad de horas extras trabajadas debe ser un número mayor o igual a 0. Intente nuevamente.")
print("La cantidad de trabajadores sin horas extras es: ", sin_extra)