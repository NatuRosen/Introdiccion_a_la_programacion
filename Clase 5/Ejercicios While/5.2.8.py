contador = int(input("Ingrese la cantidad de números primos que desea visualizar: "))
primo = 0
i = 0
while i < contador:
    for j in range(2,i):
        if i % j == 0:
            primo +=1
        if j == i-1 and primo == 0:
            print(i, " es primo") 
