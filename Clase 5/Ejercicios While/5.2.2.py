sector_valido = False
maquina_valido = False
while sector_valido == False:
    sector = int(input("Ingrese el número del sector (1-12): "))
    if 1 <= sector <= 12:
        sector_valido = True
    else:
        print("Número de sector inválido. Intente nuevamente.")
while maquina_valido == False:
    maquina = int(input("Ingrese el número de la máquina (1-31): "))
    if 1 <= maquina <= 31:
        maquina_valido = True
    else:
        print("Número de máquina inválido. Intente nuevamente.")