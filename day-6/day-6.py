# Day 6 - Tuning Trouble

# Parte 1
    # Hay que leer los datos
    # Bucle para buscar primer coincidencia de una secuencia con chars únicos en cada línea
    # Devolvemos la posición del último char + 1

#%% Lectura de datos
def leer_txt(archivo):
    with open(archivo, 'r') as f:
        datos = f.read().splitlines()
    return datos
datos_test = leer_txt('test-6.txt')
datos_input = leer_txt('input-6.txt')
#%% Bucle para buscar coincidencias
def buscar_coincidencias(linea):
    idx = 4
    my_set = set()
    while len(my_set) < 4:
        my_str = linea[idx-4:idx]
        my_set.clear()
        for char in my_str:
            my_set.add(char)
        # print(my_str, len(my_set), idx)
        idx += 1
    return idx-1
buscar_coincidencias(datos_test[0]) # 7
#%% Bucle para iterar todas las líneas
for linea in datos_test:
    print(buscar_coincidencias(linea))
# Correcto -> 7 5 6 10 11
#%% Usamos el input
for linea in datos_input:
    print(buscar_coincidencias(linea))
# Correcto -> 1109
# %%
