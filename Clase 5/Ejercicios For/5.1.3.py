cant = 0
valido = False
for i in range(100):
    while valido == False:
        num = int(input("Ingrese un numero entre 1 y 100: "))
        if num >= "A" and num <= "F":
            valido = True
    if num == "E" or num == "F":
        cant += 1
print("La cantidad de piezas defectuosas ingresadas es: ", cant)