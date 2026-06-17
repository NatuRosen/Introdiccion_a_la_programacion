sigue = True
valido = False
edad = 0
suma_edades = 0
tipo = 0
cant_1 = 0
cant_2 = 0
cant_3 = 0
while sigue == True:
    while valido == False:
        num = int(input("Ingrese un numero de legajo valido: "))
        if num == -1:
            valido = True
            sigue = False
        elif num < 10000 or num > 99999:
            valido = False
            sigue = True
        else:
            valido = True
            sigue = True
    if valido == True and sigue == True:
        nombre = input("Ingrese el nombre del paciente: ")
        while edad < 18 or edad > 100:
            edad = int(input("Ingrese la edad del paciente: "))
        suma_edades += edad
        while tipo != 1 and tipo != 2 and tipo != 3:
            tipo = int(input("Ingrese el tipo de medico que desea tomar turno (1 para endocrinologo, 2 para cardiologo, 3 para medico clinico): "))
        if tipo == 1:
            cant_1 += 1
        elif tipo == 2:
            cant_2 += 1
        elif tipo == 3:
            cant_3 += 1
    valido = False
    edad = 0
    tipo = 0
    num = 0
 
print(f"La cantidad de pacientes incriptos para el endocrinologo es: {cant_1}")
print(f"La cantidad de pacientes incriptos para el cardiologo es: {cant_2}")
print(f"La cantidad de pacientes incriptos para el medico clinico es: {cant_3}")
 
total_turnos = cant_1 + cant_2 + cant_3
 
print(f"El porcentaje de pacientes incriptos para el endocrinologo es: {(cant_1*100/total_turnos):.2f}%")
print(f"El porcentaje de pacientes incriptos para el cardiologo es: {(cant_2*100/total_turnos):.2f}%")
print(f"El porcentaje de pacientes incriptos para el medico clinico es: {(cant_3*100/total_turnos):.2f}%")
 
print(f"El promedio de edad de los pacientes incriptos es: {(suma_edades/total_turnos):.2f}")
 
if cant_1 >= cant_2 and cant_1 >= cant_3:
    print("El tipo de medico con mas pacientes inscriptos es el endocrinologo")
elif cant_2 >= cant_1 and cant_2 >= cant_3:
    print("El tipo de medico con mas pacientes inscriptos es el cardiologo")
else:
    print("El tipo de medico con mas pacientes inscriptos es el medico clinico")
 
if cant_3 <= cant_1 and cant_3 <= cant_3:
    print("El tipo de medico con mas pacientes inscriptos es el medico clinico")
elif cant_2 <= cant_1 and cant_2 <= cant_3:
    print("El tipo de medico con mas pacientes inscriptos es el cardiologo")
else:
    print("El tipo de medico con mas pacientes inscriptos es el medico clinico")