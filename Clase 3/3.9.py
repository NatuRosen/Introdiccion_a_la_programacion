fecha = input("Ingrese una fecha en formato ddmmaa: ")
dia = int(fecha[0:2])
mes = int(fecha[2:4])
año = int(fecha[4:])
if mes >= 1 and mes <= 12:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if dia >= 1 and dia <= 31:
            print("La fecha es válida.")
        else:
            print("La fecha no es válida.")
    elif mes in [4, 6, 9, 11]:
        if dia >= 1 and dia <= 30:
            print("La fecha es válida.")
        else:
            print("La fecha no es válida.")
    elif mes == 2:
        if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
            if dia >= 1 and dia <= 29:
                print("La fecha es válida.")
            else:
                print("La fecha no es válida.")
        else:
            if dia >= 1 and dia <= 28:
                print("La fecha es válida.")
            else:
                print("La fecha no es válida.")