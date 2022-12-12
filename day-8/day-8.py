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
def calc_arbol_visible():
    pass
#%% Bucle de árboles interiores
    # Entre 1 y n-1 si usamos range
def calc_interiores():
    arboles_visibles_interior = 0
    return arboles_visibles_interior
#%% Retornamos total de visibles
print(calc_borde() + calc_interiores()) # 16 + 5 = 21
