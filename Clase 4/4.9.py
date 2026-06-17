par = 0
impar = 0
num = None
while num != -1:
    num = int(input("Ingrese el número de finalización de su patente (o -1 para terminar): "))
    if num != -1:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print("La cantidad de patentes con número par es: ", par)
print("La cantidad de patentes con número impar es: ", impar)