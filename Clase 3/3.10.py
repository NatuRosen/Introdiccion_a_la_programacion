sueldo_basico = int(input("Ingrese su sueldo básico: "))
antiguedad = int(input("Ingrese su antigüedad en años: "))
estado_civil = int(input("Ingrese su estado civil (1: Soltero, 2: Casado): "))
sueldo = 0
if estado_civil == 1:
    sueldo = sueldo_basico * antiguedad * 1.05
elif estado_civil == 2:
    sueldo = sueldo_basico * antiguedad * 1.70
jubilacion = sueldo * 0.11
obra_social = sueldo * 0.03
sindicato = sueldo * 0.03
sueldo_neto = sueldo - jubilacion - obra_social - sindicato
if estado_civil == 1:
    print("Estado civil: Soltero")
elif estado_civil == 2:
    print("Estado civil: Casado")
print("Sueldo basico: ", sueldo_basico)
print("Antigüedad: ", antiguedad, "años")
print("Jubilación: ", jubilacion)
print("Obra social: ", obra_social)
print("Sindicato: ", sindicato)
print("El sueldo neto es: ", sueldo_neto)