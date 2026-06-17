num = 0
valido = False
edad = 0
termino = False
invitados_valido = False
recaudacion_natural = 0
recaudacion_climatizada = 0
recaudacion_olimpica = 0
cant_natu = 0
cant_clima = 0
cant_olim = 0
sigue = True
 
while sigue == True:
    while valido == False and termino == False:
        num = int(input("Ingrese un numero de reserva: "))
        if num == -1:
            print("Termino el programa")
            termino = True
            sigue = False
        elif num < 1000 or num > 9999:
            valido = False
        else:
            valido = True
 
    if valido == True and termino == False:
        while edad < 18 or edad > 65:
            edad = int(input("Ingrese su edad: "))
        horas_pileta = int(input("Ingrese las horas por las que desea reservar la pileta: "))
        pileta = int(input("Ingrese la pileta que desea reservar (1 para natural, 2 para climatizada, 3 para olimpica): "))
        while invitados_valido == False:
            invitados = int(input("Ingrese la cantidad de invitados: "))
            if pileta == 1 and invitados > 15:
                invitados_valido = False
            elif pileta == 2 and invitados > 10:
                invitados_valido = False
            elif pileta == 3 and invitados > 20:
                invitados_valido = False
            else: invitados_valido = True
   
        if pileta == 1:
            recaudacion_natural += 30000 * horas_pileta * invitados
            cant_natu += 1
        elif pileta == 2:
            recaudacion_climatizada += 50000 * horas_pileta * invitados
            cant_clima += 1
        elif pileta == 3:
            recaudacion_olimpica += 80000 * horas_pileta * invitados
            cant_olim += 1
   
    valido = False
    termino = False
    invitados_valido = False
    edad = 0
    pileta = 0
 
print(f"El total recaudado de la pileta natural fue: ${recaudacion_natural}")
print(f"El total recaudado de la pileta climatizada fue: ${recaudacion_climatizada}")
print(f"El total recaudado de la pileta olimpica fue: ${recaudacion_olimpica}")
 
mas_alquilada_cant = max(cant_natu, cant_clima, cant_olim)
if mas_alquilada_cant == cant_natu:
    mas_alquilada = "Natural"
elif mas_alquilada_cant == cant_clima:
    mas_alquilada = "Climatizada"
elif mas_alquilada_cant == cant_olim:
    mas_alquilada = "Olimpica"
print(f"La pileta que mas veces fue alquilada es la pileta {mas_alquilada}")
if cant_natu == cant_clima or cant_natu == cant_olim or cant_clima == cant_olim or cant_natu == cant_clima == cant_olim:
    print("Hay piletas que fueron alquiladas la misma cantidad de veces")
else:
    print("No hay piletas que fueron alquiladas la misma cantidad de veces")
total_reservas = cant_natu+cant_clima+cant_olim
print("El total de reservas realizadas fue: ", total_reservas)
print(f"El porcentaje de uso de la pileta natural fue de un {(cant_natu*100/total_reservas):.2f}%")
print(f"El porcentaje de uso de la pileta climatizada fue de un {(cant_clima*100/total_reservas):.2f}%")
print(f"El porcentaje de uso de la pileta olimpica fue de un {(cant_olim*100/total_reservas):.2f}%")