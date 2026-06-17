sigue = "S"
total = 0
cantidad = 0
while sigue == "S":
    legajo = int(input("Ingrese el numero de legajo del empleado: "))
    sueldo_basico = int(input("Ingrese el sueldo basico del empleado: "))
    antiguedad = int(input("Ingrese los años de antiguedad del empleado: "))
    hijos = int(input("Ingrese la cantidad de hijos del empleado: "))
    certificacion = input("Ingrese si el empleado posee una certificacion técnica superior (S/N): ")
    if antiguedad >= 10:
        sueldo_basico *= 1.1
    if hijos >= 2:
        sueldo_basico *= 1.1
    elif hijos == 1:
        sueldo_basico *= 1.05
    if certificacion == "S":
        sueldo_basico *= 1.05
    total += sueldo_basico
    cantidad += 1
    print(f"El sueldo final del empleado con legajo {legajo} es: ${sueldo_basico:.2f}")
    sigue = input("Desea ingresar otro empleado? (S/N): ")
if cantidad > 0:
    print(f"El sueldo promedio de los empleados es: ${total/cantidad:.2f}")