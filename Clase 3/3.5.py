n1 = int(input("Ingrese la primera nota: "))
n2 = int(input("Ingrese la segunda nota: "))
if n1 < 0 or n1 > 10:
    print("La primera nota es inválida.")
elif n2 < 0 or n2 > 10:
    print("La segunda nota es inválida.")
elif n1 >= 7 and n2 >= 7:
    print("Promociona")
elif n1 >= 4 and n2 >= 4:
    print("Aprueba")
else:
    print("Debe recuperar")