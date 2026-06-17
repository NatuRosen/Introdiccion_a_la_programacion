num = int(input("Ingrese el precio del producto: "))
descuento = int(input("Ingrese el código numérico del producto (1 o 2): "))
if descuento == 1:
    precio_final = num * 0.8
else:
    precio_final = num
print("El precio final del producto es: ", precio_final)