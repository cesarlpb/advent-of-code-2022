# Modificar función de lecttura para almacenar en un diccionario
    # dict = { 1: "NZ", 2: "DCM", 3: "P"}
# Fn para entender los pasos a realizar en lista de listas o tuplas de 3 elementos
    # pasos = [ [1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]
    # cada uno de los pasos contiene: # cajas a mover, desde col, hasta col
# Fn para mover cajas
    # mover cajas de una columna a otra usando pasos -> nuevo_dict
# Bucle para que lea los primeros ( = caja de arriba) chars de cada value del nuevo_dict -> str de 9 chars

#%% Leer inputo o test
def leer_txt(archivo):
    with open(archivo, 'r') as f:
        input = f.read().splitlines()
    return input

# sabemos leer el archivo por filas -> fn -> retorna primera parte y segunda parte // dos listas
 # determinamos que la primera parte, las cajas por cols, es un diccionario y hasta donde aparecen los primeros números/digitos -> fn -> dict
 # segunda parte: pasos -> otra fn -> lista de listas