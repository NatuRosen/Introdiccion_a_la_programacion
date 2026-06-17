valido = False
while valido == False:
    vocal = input("Ingrese una vocal (en mayúscula) o 'f' para finalizar: ")
    if vocal == "A":
        for i in range(5):
            if i == 0:
                print("  A  ")
            elif i == 1:
                print(" A A ")
            elif i == 2:
                print("AAAAA")
            elif i == 3:
                print("A   A")
    elif vocal == "E":
        for i in range(5):
            if i == 0:
                print("EEEEE")
            elif i == 1:
                print("E    ")
            elif i == 2:
                print("EEEEE")
            elif i == 3:
                print("E    ")
            elif i == 4:
                print("EEEEE")
    elif vocal == "I":
        for i in range(5):
            if i == 0:
                print("  I  ")
            elif i == 1:
                print("     ")
            elif i == 2:
                print("  I  ")
            elif i == 3:
                print("  I  ")
            elif i == 4:
                print("  I  ")
    elif vocal == "O":
        for i in range(5):
            if i == 0:
                print(" OOO ")
            elif i == 1:
                print("O   O")
            elif i == 2:
                print("O   O")
            elif i == 3:
                print("O   O")
            elif i == 4:
                print(" OOO ")
    elif vocal == "U":
        for i in range(5):
            if i == 0:
                print("U   U")
            elif i == 1:
                print("U   U")
            elif i == 2:
                print("U   U")
            elif i == 3:
                print("U   U")
            elif i == 4:
                print(" UUU")
    elif vocal == "f":
        print("Terminando el programa...")
        valido = True
    else:
        print("Vocal inválida. Vuelva a ingresarla.")