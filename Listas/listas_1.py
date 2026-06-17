temp = []
temo_aux = []
total = None
prom = None
cantidad = 5

def ingresar(cantidad, temp):
    lista = []
    for i in range(cantidad):
        num = int(input(f"Ingrese el número {i+1}: "))
        lista.append(num)
    temp = lista
    return temp

def copiar_aux (lista, temp_aux):
    aux = []
    for i in range(len(lista)):
        aux.append(lista[i])
    temp_aux = aux
    return temp_aux

def total (lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    total = suma
    return total

def promedio (suma, cantidad, prom):
    prom = suma/cantidad
    return prom

def bajo_cero(lista):
    contador = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            contador += 1
    return contador

def suma(lista1, lista2):
    dif = []
    for i in range(len(lista1)):
        dif.append(lista1[i] + lista2[i])
    return dif

def inverso(lista):
    inv = []
    for i in range(len(lista)-1, -1, -1):
        inv.append(lista[i])
    print(inv)
    return inv

ingresar(cantidad)
print()
inverso()