cant = int(input("Ingrese la cantidad de artículos: "))
cable_corto = cant * 0.5
cable_estandar = cant * 0.3
bobina = cant - cable_corto - cable_estandar
print("La cantidad de cables cortos es: ", cable_corto)
print("La cantidad de cables estándar es: ", cable_estandar)
print("La cantidad de bobinas es: ", bobina)