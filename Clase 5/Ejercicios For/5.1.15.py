maquina_mas_produccion = 0
for i in range(10):
    codigo = int(input(f"Ingrese el código de la máquina {i+1}: "))
    produccion = int(input(f"Ingrese la producción de la máquina {codigo}: "))
    if produccion > maquina_mas_produccion:
        maquina_mas_produccion = codigo
print("El código de la máquina con mayor producción es: ", maquina_mas_produccion)