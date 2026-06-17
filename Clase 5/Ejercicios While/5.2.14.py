legajo = None
cant_viejos = 0
sueldo_mayor = 0
legajo_mayor = None
cant_hombres = 0
cant_mujeres = 0
while legajo != 0:
    tarifa_valida = False
    antiguedad_valida = False
    sexo_valido = False
    riesgo_valido = False
    legajo = int(input("Ingrese el número de legajo del empleado (0 para finalizar): "))
    if legajo != 0:
        while tarifa_valida == False:
            tarifa_basica = (int(input("Ingrese la tarifa básica del empleado: ")))
            if tarifa_basica >= 1000 and tarifa_basica <= 5000:
                tarifa_valida = True
            else:
                print("Tarifa básica inválida. Vuelva a ingresarla.")
        while antiguedad_valida == False:
            antiguedad = int(input("Ingrese los años de antigüedad del empleado: "))
            if antiguedad >= 0:
                antiguedad_valida = True
                if antiguedad > 10:
                    cant_viejos += 1
            else:
                print("Antigüedad inválida. Vuelva a ingresarla.")
        while sexo_valido == False:
            sexo = input("Ingrese el sexo del empleado (M/F): ")
            if sexo == "M" or sexo == "F":
                sexo_valido = True
                if sexo == "M":
                    cant_hombres += 1
                else:
                    cant_mujeres += 1
            else:
                print("Sexo inválido. Vuelva a ingresarlo.")
        while riesgo_valido == False:
            riesgo = int(input("Ingrese el nivel de riesgo del empleado (1-5): "))
            if riesgo >= 1 and riesgo <= 5:
                riesgo_valido = True
            else:
                print("Nivel de riesgo inválido. Vuelva a ingresarla.")
        sueldo = tarifa_basica
        if riesgo == 2 or riesgo == 3:
            sueldo += 500
        elif riesgo == 4:
            sueldo *= 1.1
        elif riesgo == 5:
            sueldo *= 1.3
        if antiguedad > 10:
            sueldo *= 1.1
        if sueldo > sueldo_mayor:
            sueldo_mayor = sueldo
            legajo_mayor = legajo
        print(f"El sueldo final del empleado con legajo {legajo} es: ${sueldo:.2f}")
        
empleados_totales = cant_hombres + cant_mujeres
print(f"La cantidad de empleados con más de 10 años de antigüedad es: {cant_viejos}")
print(f"El legajo del empleado con el sueldo más alto es: {legajo_mayor}, con un sueldo de ${sueldo_mayor:.2f}")
print(f"La proporción de empleados hombres es: {(cant_hombres*100/(empleados_totales)):.2f}%")
print(f"La proporción de empleados mujeres es: {(cant_mujeres*100/(empleados_totales)):.2f}%")