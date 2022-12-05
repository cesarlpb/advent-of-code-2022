# Day 4 - https://adventofcode.com/2022/day/4

# X Leer txt
# Crear rangos numéricos de los intervalos
# Iterar sobre el rango más corto -> verificar si todos sus números están contenidos en el otro
# Aumentamos contador de incluídos
# Retornamos contador
#%% Leer inputo o test
def leer_txt(archivo):
    with open(archivo, 'r') as f:
        input = f.read().splitlines()
    return input
#%% Reordenamos secuencias

def completar_secuencias(lista):
    nueva_lista = []
    lim_inf = lista[0]
    lim_sup = lista[1]
    for i in range(int(lim_inf), int(lim_sup)+1):
        nueva_lista.append(i)
    return nueva_lista

def reordenar_secuencias(linea):
    linea = linea.split(',')
    linea = [x.split('-') for x in linea]
    print(linea[0])
    izquierda  = completar_secuencias(linea[0])
    derecha = completar_secuencias(linea[1])
    print(izquierda, derecha)
    
reordenar_secuencias("2-4,6-8")