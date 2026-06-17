for i in range(1,9001):
    suma_divisores = 0
    for j in range(1,i):
        if i % j == 0:
            suma_divisores += j
    if suma_divisores == i:
        print(i)