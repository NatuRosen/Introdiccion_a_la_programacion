n1 = None
n2 = None
n3 = None
n4 = None
n5 = None
valido = False
sigue = True
capicua_3 = 0
capicua_5 = 0
while sigue == True:
    for i in range(5):
        while valido == False:
            num = int(input(f"Ingrese el {i+1} número del código: "))
            if num >= 0 and num <= 9:
                valido = True
            else:
                print("El numero debe estar entre 0 y 9. Intente nuevamente.")
        if i == 0:
            n1 = num
        elif i == 1:
            n2 = num
        elif i == 2:
            n3 = num
        elif i == 3:
            n4 = num
        elif i == 4:
            n5 = num
        valido = False
    if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0 and n5 == 0:
        sigue = False
    elif n2 == n4:
        if n1 == n5:
            capicua_5 += 1
        else:
            capicua_3 += 1
    n1 = None
    n2 = None
    n3 = None
    n4 = None
    n5 = None
print("La cantidad de códigos capicúa de 3 dígitos es: ", capicua_3)
print("La cantidad de códigos capicúa de 5 dígitos es: ", capicua_5)