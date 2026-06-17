paginas = int(input("Ingrese el número de páginas del libro: "))
if paginas > 0 and paginas <= 300:
    costo = 5000 + (paginas * 32)
    print("El costo del libro es: ", costo)
elif paginas >= 300 and paginas < 600:
    costo = 5000 + (paginas * 32) + 1200
    print("El costo del libro es: ", costo)
elif paginas >= 600:
    costo = 5000 + (paginas * 32) + 1200 + 3360
    print("El costo del libro es: ", costo)
else:
    print("Número de páginas no válido.")