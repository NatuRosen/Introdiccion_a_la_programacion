temp = None
max_temp = None
max_pos = None
min_temp = None
min_pos = None
contador = 0
while temp != -50:
    temp = int(input("Ingrese la temperatura (en grados Celsius) o -50 para salir: "))
    if temp != -50:
        if max_temp is None or temp > max_temp:
            max_temp = temp
            max_pos = contador
        if min_temp is None or temp < min_temp:
            min_temp = temp
            min_pos = contador
        contador += 1

print(f"La temperatura máxima fue {max_temp}°C y se registró en la posición {max_pos}.")
print(f"La temperatura mínima fue {min_temp}°C y se registró en la posición {min_pos}.")