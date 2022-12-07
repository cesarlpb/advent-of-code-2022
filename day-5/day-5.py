# Modificar función de lecttura para almacenar en un diccionario
    # dict = { 1: "NZ", 2: "DCM", 3: "P"}
# Fn para entender los pasos a realizar en lista de listas o tuplas de 3 elementos
    # pasos = [ [1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]
    # cada uno de los pasos contiene: # cajas a mover, desde col, hasta col
# Fn para mover cajas
    # mover cajas de una columna a otra usando pasos -> nuevo_dict
# Bucle para que lea los primeros ( = caja de arriba) chars de cada value del nuevo_dict -> str de 9 chars

#%% Leer inputo o test
def leer_txt_modificado(archivo):
    with open(archivo, 'r') as f:
        datos = f.read().splitlines()
    idx = 0
    cols_idx = 0
    while idx < len(datos):
        if datos[idx].replace(" ", "").isdigit():
            cols_idx = idx
            break
        idx += 1
    return (datos[:cols_idx], datos[cols_idx+2:], cols_idx)

# sabemos leer el archivo por filas -> fn -> retorna primera parte y segunda parte // dos listas
 # X determinamos que la primera parte, las cajas por cols, es un diccionario y hasta donde aparecen los primeros números/digitos -> fn -> dict
 # X segunda parte: pasos -> otra fn -> lista de listas
cajas, pasos, num_cols = leer_txt_modificado('test-5.txt')
print("cajas:\n", cajas)
pasos_lista = []
for paso in pasos:
    temp = paso.replace("move ", "").replace(" from ", " ").replace(" to ", " ").split(" ")
    temp = [int(i) for i in temp]
    pasos_lista.append(temp)
print("pasos:\n", pasos_lista)
print("cols:", num_cols)
#%% Diccionario -> cada value es una lista de chars, cada char es una caja
    # Convenio: como las primeras filas del txt son cajas "arriba"
    #           entonces el primer char de cada value es la caja de arriba
    # dict = { 1: "NZ", 2: "DCM", 3: "P"}
    # Iteraciones:
    # dict = { 1: "", 2: "D", 3: ""}
    # dict = { 1: "N", 2: "DC", 3: ""}
    # dict = { 1: "NZ", 2: "DCM", 3: "P"}
    #cols (j) key (i)
    # j = 1 + 4*(i)
    # 1         1 
    # 5         2
    # 9         3
def crear_dict(cajas, num_cols):
    my_dict = {}
    dict_ij = {}
    
    for i in range(num_cols):
        dict_ij[1 + 4 * (i)] = i+1
        my_dict[i+1] = ""
    print(dict_ij)
    i = 0
    while i < len(cajas):
        j = 1
        linea = cajas[i]
        while j < len(linea):
            if linea[j] != " ":
                temp = dict_ij[j]
                my_dict[temp] += linea[j]
            j += 4
        i += 1
    return my_dict
my_dict = crear_dict(cajas, num_cols)
print(my_dict)
#%% Fn para mover cajas
    # input: pasos_lista
    # realizar los movimientos de cajas
    # llegar al resultado final

#%% Entregar las cajas de arriba de cada columna
    # los primeros caracteres de cada value del dict
