caracter= None
numero = 0
mayus = 0
minus = 0
otro = 0
while caracter != "*":
    caracter = input("Ingrese un caracter (ingrese '*' para finalizar): ")
    if caracter >= "0" and caracter <= "9":
        numero += 1
    elif caracter >= "A" and caracter <= "Z":
        mayus += 1
    elif caracter >= "a" and caracter <= "z":
        minus += 1
    else:
        otro += 1
print("La cantidad de caracteres numéricos ingresados es: ", numero)
print("La cantidad de letras mayúsculas ingresados es: ", mayus)
print("La cantidad de letras minúsculas ingresados es: ", minus)
print("La cantidad de caracteres especiales ingresados es: ", otro)