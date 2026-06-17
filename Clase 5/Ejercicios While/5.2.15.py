fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
cant_plantas = int(input("Ingrese la cantidad de plantas a auditar: "))
empleados_metalurgica = 0
empleados_tecnologica = 0
mujeres_tecnologica = 0
malas_opiniones = 0
empleados_totales = 0
mayor_edad = 0
dni_mayor = 0
planta_buenas_opiniones = None

if cant_plantas > 0:
    for i in range(cant_plantas):
        planta_valida = False
        empleados_valida = False
        rubro_valido = False
        while planta_valida == False:
            nro_planta = int(input(f"Ingrese el número de planta {i+1}: "))
            if nro_planta > 0:
                planta_valida = True
        while empleados_valida == False:
            empleados = int(input(f"Ingrese la cantidad de empleados en la planta {nro_planta}: "))
            if empleados > 0:
                empleados_valida = True
        while rubro_valido == False:
            rubro = input(f"Ingrese el rubro de la planta {nro_planta} (T/M): ")
            if rubro == "T" or rubro == "M":
                if rubro == "M":
                    metalurgica += 1
                rubro_valido = True
        j = 1
        encuestados = 0
        while j <= empleados or dni == 0:
            opiniones_buenas = 0
            dni = int(input(f"Ingrese el DNI del empleado {j+1} de la planta {nro_planta}: "))
            if dni == 0:
                j = empleados + 1
            else:
                j += 1
                encuestados += 1
                nacimiento = int(input(f"Ingrese el año de nacimiento del empleado {j} de la planta {nro_planta}: "))
                if nacimiento < mayor_edad:
                    mayor_edad = nacimiento
                    dni_mayor = dni
                sexo = input(f"Ingrese el sexo del empleado {j} de la planta {nro_planta} (M/F): ")
                if sexo == "F" and rubro == "T":
                    mujeres_tecnologica += 1
                opinion = input("Ingrese la opinión del empleado sobre las normas de seguridad (B/M)")
                if opinion == "M":
                    malas_opiniones += 1
                elif opinion == "B":
                    opiniones_buenas += 1
        if planta_buenas_opiniones == None or opiniones_buenas > planta_buenas_opiniones:
            planta_buenas_opiniones = opiniones_buenas
            planta_mayor_opiniones = nro_planta
        if encuestados > 0:
            print(f"El porcentaje de empleados encuestados en la planta {nro_planta} es: {(encuestados*100/empleados):.2f}%")
        else:
            print(f"No se encuestaron empleados en la planta {nro_planta}")
        if rubro == "M":
            empleados_metalurgica += j
        empleados_totales += j
        
print(f"La cantidad de plantas metalúrgicas auditadas es: {metalurgica}")
print(f"La cantidad total de empleados encuestados en las plantas metalúrgicas es: {empleados_metalurgica}")
print(f"La cantidad total de mujeres encuestadas en las plantas tecnológicas es: {mujeres_tecnologica}")
print(f"La cantidad de empleados que dieron una mala opinión sobre las normas de seguridad es: {malas_opiniones}")
print(f"El empleado con mayor edad tiene DNI {dni_mayor} y nació en el año {mayor_edad}")
print(f"La planta con mayor cantidad de opiniones buenas sobre las normas de seguridad es la planta {planta_mayor_opiniones}, con {planta_buenas_opiniones} opiniones buenas.")