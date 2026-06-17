cant = int(input("Ingrese la cantidad de empanadas que desee comprar: "))
precio_docena = 8000 * (cant // 12)
precio_unitario = 800 * (cant % 12)
total = precio_docena + precio_unitario
print("El total a pagar es: ", total)