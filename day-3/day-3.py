# X Leer txt
# X Separar en mitades
# X Iterar ambas mitades para determinar qué caracter se repite
    # X print -> el caracter que se repite
# Calcular prioridad
# Calcular sumas de prioridades

#%% Función para leer txt y retornar input separado por salto de línea
# param archivo: archivo a leer
# return: input = lista de strings (cada char es un artículos)
def leer_txt(archivo):
    with open(archivo, 'r') as f:
        input = f.read().splitlines()
    return input
#%% Función para separar en mitades ignorando el caracter de en medio
# param lista_de_articulos: línea del input
# return: tupla con lista de artículos (izquierda y derecha)
def separar_mitades(lista_de_articulos):
    esImpar = len(lista_de_articulos) % 2 != 0
    mitad = len(lista_de_articulos) // 2
    if esImpar:
        izquierda = lista_de_articulos[0 : mitad-1]
        derecha = lista_de_articulos[mitad : ]
    else:
        izquierda = lista_de_articulos[0 : mitad]
        derecha = lista_de_articulos[mitad : ]
    return (izquierda, derecha)
#%% Buscamos coincidencias entre las dos mitades
def buscar_coincidencias(izquierda, derecha):
    c_izquierda, c_derecha = [], []
    for i in izquierda:
        if i in derecha:
            c_izquierda.append(True)
        else:
            c_izquierda.append(False)
    for i in derecha:
        if i in izquierda:
            c_derecha.append(True)
        else:
            c_derecha.append(False)
    return (c_izquierda, c_derecha)
#%% Test de separar_mitades y buscar_coincidencias con un dato
datos_test = leer_txt('test-3.txt')
concidencias_test = []
for i in range(len(datos_test)):
    izquierda, derecha = separar_mitades(datos_test[i])
    c_izquierda, c_derecha = buscar_coincidencias(izquierda, derecha)
    concidencias_test.append((c_izquierda, c_derecha))
# Descomentar para comprobar coincidencias
# for i in range(len(concidencias_test)):
#     print(f"\n{i}\n{concidencias_test[i][0]}\n{concidencias_test[i][1]}")
# Verificamos que las coincidencias son únicas
#%% Definimos una función para quedarnos con la primera coincidencia
def primera_coincidencia(izquierda, derecha):
    for char in izquierda:
        if char in derecha:
            return char
    return None
datos_test = leer_txt('test-3.txt')
for lista in datos_test:
    izquierda, derecha = separar_mitades(lista)
    print(primera_coincidencia(izquierda, derecha))
# Correcto en datos de test
#%% Cálculo de prioridades
a_z = 'abcdefghijklmnopqrstuvwxyz'
A_Z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def calcular_prioridad(char):
    if char in a_z:
        return a_z.index(char)+1
    elif char in A_Z:
        return A_Z.index(char)+27
    else:
        return None
# Test calcular_prioridad
# 16 (p), 38 (L), 42 (P), 22 (v), 20 (t) y 19 (s); 
# la suma de estos es 157
datos_test = leer_txt('test-3.txt')
prioridades = []
for lista in datos_test:
    izquierda, derecha = separar_mitades(lista)
    char = primera_coincidencia(izquierda, derecha)
    prioridades.append(calcular_prioridad(char))
print(prioridades)      # [16, 38, 42, 22, 20, 19]
print(sum(prioridades)) # 157
# Correcto en datos de test
#%% Cálculo de suma de prioridades para el input completo
datos_input = leer_txt('input-3.txt')
prioridades = []
for lista in datos_input:
    izquierda, derecha = separar_mitades(lista)
    char = primera_coincidencia(izquierda, derecha)
    prioridades.append(calcular_prioridad(char))
# print(prioridades)      
print(sum(prioridades)) 
# %%
