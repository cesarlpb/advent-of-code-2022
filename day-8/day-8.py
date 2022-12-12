# Day 8 - Treetop Tree House
# Cada dígito en la lista de datos representa un árbbol del bosque de altura de 0 a 9.

#%% Leer datos
def leer_txt(archivo):
    with open(archivo, "r") as f:
        datos = f.read().splitlines()
    return datos
datos_test = leer_txt("test-8.txt")
datos_input = leer_txt("input-8.txt")
# Parte 1
#%% Calcular borde - árboles en borde
# Opción 1 - Calcular borde por deducción -> n*2 + (n-2)*2
def calc_borde(n):
    return n*2 + (n-2)*2
# Opción 2 - Calcular borde por bucle
def calc_borde_2(datos):
    arboles_en_borde = 0
    for fila in range(1, len(datos)-1):
        arboles_en_borde += 2
    return arboles_en_borde + 2*len(datos[0]) 
print(5, calc_borde(5), calc_borde_2(datos_test))
print(99, calc_borde(99), calc_borde_2(datos_input))
#%% Calcular si el arbol es visible
    # se tienen que verificar las 4 direcciones principales -> filas y columnas
    # Visible := que el árbol tenga mayor altura que los árboles que están en su alrededor
def es_arbol_visible(fila, columna, datos):
    es_visible_izq, es_visible_der, es_visible_arriba, es_visible_abajo = True, True, True, True
    arbol = datos[fila][columna]
    # Izquierda y derecha
    arboles_fila = datos[fila]
    col = 0
    while col < len(arboles_fila) and (es_visible_izq or es_visible_der):
        if col < columna and arboles_fila[col] > arbol and col in range(1, len(arboles_fila)-1):
            es_visible_izq = False
        elif col > columna and arboles_fila[col] > arbol and col in range(1, len(arboles_fila)-1):
            es_visible_der = False
            break
        col += 1
    # Arriba y abajo
    fil = 0
    while fil < len(datos) and (es_visible_arriba or es_visible_abajo):
        if fil < fila and datos[fil][columna] > arbol and fil in range(1, len(datos)-1):
            es_visible_arriba = False
        elif fil > fila and datos[fil][columna] > arbol and fil in range(1, len(datos)-1):
            es_visible_abajo = False
            break
        fil += 1
    return es_visible_arriba
#%% Bucle de árboles interiores
    # Entre 1 y n-1 si usamos range
        # salir del bucle si no es visible
def calc_interiores(datos):
    arboles_visibles_interior = 0
    fila, columna = 1, 1
    es_visible = False
    while fila < len(datos)-1:
        columna = 1
        while columna < len(datos[0]) - 1:
            es_visible = es_arbol_visible(fila, columna, datos)
            if es_visible:
                arboles_visibles_interior += 1
                print("V", end=" ")
            else:
                print("N", end=" ")
            columna += 1
        print("")
        fila += 1
    return arboles_visibles_interior
print("Árboles visibles:", calc_interiores(datos_test))
#%% Retornamos total de visibles
print(calc_borde() + calc_interiores()) # 16 + 5 = 21
