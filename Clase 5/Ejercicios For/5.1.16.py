precio_caro = 0
codigo_caro = 0
precio_barato = None
num = int(input("Ingrese la cantidad de números a ingresar: "))
for i in range(num):
    codigo = int(input(f"Ingrese el código del producto {i+1}: "))
    precio = float(input(f"Ingrese el precio del producto {codigo}: "))
    if precio > precio_caro:
        precio_caro = precio
        codigo_caro = codigo
    if precio_barato is None or precio < precio_barato:
        precio_barato = precio
print("El código del producto más caro es: ", codigo_caro)
print("El precio del producto más barato es: $", precio_barato)