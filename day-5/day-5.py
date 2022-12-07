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
            cols_idx = len(datos[idx].replace(" ", ""))
            break
        idx += 1
    return (datos[:cols_idx], datos[cols_idx+2:], cols_idx)

# sabemos leer el archivo por filas -> fn -> retorna primera parte y segunda parte // dos listas
 # X determinamos que la primera parte, las cajas por cols, es un diccionario y hasta donde aparecen los primeros números/digitos -> fn -> dict
 # X segunda parte: pasos -> otra fn -> lista de listas
cajas, pasos, num_cols = leer_txt_modificado('test-5.txt')
print("cajas:\n", cajas)
def calc_pasos_lista(pasos):
    pasos_lista = []
    for paso in pasos:
        temp = paso.replace("move ", "").replace(" from ", " ").replace(" to ", " ").split(" ")
        temp = [int(i) for i in temp]
        pasos_lista.append(temp)
    return pasos_lista
pasos_lista = calc_pasos_lista(pasos)
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
def crear_dict(cajas, num_cols_input):
    my_dict = {}
    dict_ij = {}
    
    for i in range(0,num_cols_input): 

        dict_ij[1 + 4 * i] = i+1
        my_dict[i+1] = ""
        print(i+1, 1 + 4 * i)
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

pos_iniciales = crear_dict(cajas, num_cols)
print(pos_iniciales)
#%% Fn para mover cajas
    # input: pasos_lista
    # realizar los movimientos de cajas
    # llegar al resultado final

    # dict = { 1: "NZ", 2: "DCM", 3: "P"}
    # dict = { 1: "NZ", 2: "CM", 3: "P"}
    # dict = { 1: "DNZ", 2: "CM", 3: "P"}
    # ...
def mover_cajas(pasos_lista_input, my_dict):
    for paso in pasos_lista_input:
        num_cajas, desde, hasta = paso
        cajas_a_mover = my_dict[desde][:num_cajas]
        my_dict[desde] = my_dict[desde][num_cajas:]
        my_dict[hasta] = cajas_a_mover[::-1] + my_dict[hasta]
        # print(my_dict)
    return my_dict

pos_finales = mover_cajas(pasos_lista, pos_iniciales) # correcto -> CMZ
#%% Entregar las cajas de arriba de cada columna
    # los primeros caracteres de cada value del dict
for key, value in pos_finales.items():
    print(value[0], end="")
# CMZ -> TODO: hay que evitar que el caso de test nos genere 4 keys
#%% Realizamos la ordenación con el input
cajas_input, pasos_input, num_cols_input = leer_txt_modificado('input-5.txt')
pos_iniciales_input = crear_dict(cajas_input, 9)
pasos_input_lista = calc_pasos_lista(pasos_input)
pos_finales_input = mover_cajas(pasos_input_lista, pos_iniciales_input)
cajas_superiores = ""
for key, value in pos_finales_input.items():
    cajas_superiores += value[0]
print(cajas_superiores) #-> SHQWSRBDL # ha cambiado la salida a RZTGHGFDG
# %%
