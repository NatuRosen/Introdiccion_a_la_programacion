a_favor = int(input("Ingrese el número de votos a favor: "))
en_contra = int(input("Ingrese el número de votos en contra: "))
total_votos = a_favor + en_contra
porc_a_favor = (a_favor / total_votos) * 100
porc_en_contra = (en_contra / total_votos) * 100
if porc_a_favor > porc_en_contra:
    print("La ley fue aprobada con un porcentaje de: ", porc_a_favor, "%")
else:
    print("La ley fue rechazada con un porcentaje de: ", porc_en_contra, "%")