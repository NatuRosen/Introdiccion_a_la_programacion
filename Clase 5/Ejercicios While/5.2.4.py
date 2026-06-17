costo_valido = False
codigo_valido = False
sigue = True
emp_exp = 0
cam_prop = 0
tren = 0
while sigue == True:
    while costo_valido == False:
        costo = int(input("Ingrese el costo de la carga: "))
        if costo > 0:
            costo_valido = True
        else:
            print("El costo debe ser mayor a 0. Intente nuevamente.")
    if costo_valido == True:
        while codigo_valido == False and sigue == True:
            codigo = input("Ingrese un código que indica la forma de envío (C, E, T, o F para cortar): ")
            if codigo == "C":
                codigo_valido = True
                costo *= 1.2
                cam_prop += costo
            elif codigo == "E":
                codigo_valido = True
                costo *= 0.9
                emp_exp += costo
            elif codigo == "T":
                codigo_valido = True
                costo *= 1.12
                tren += costo
            elif codigo == "F":
                sigue = False
            else:
                print("El código debe ser C, E o T. Intente nuevamente.")
    costo_valido = False
    codigo_valido = False
    
print("Fletes con Empresa Externa: $", emp_exp)
print("Fletes con Camión Propio: $", cam_prop)
print("Fletes por Tren: $", tren)
print("Total bruto de Fletes: $", emp_exp + cam_prop + tren)
print("Importe de retenciones (IVA): $", (emp_exp + cam_prop + tren) * 0.21)