# Day 4 - https://adventofcode.com/2022/day/4

# X Leer txt
# X Crear rangos numéricos de los intervalos
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
    izquierda  = completar_secuencias(linea[0])
    derecha = completar_secuencias(linea[1])
    return (izquierda, derecha)
    
#%% Bucle para comprobar secuencias en test.txt
datos_test = leer_txt('test-4.txt')
for i in datos_test:
    izquierda, derecha = reordenar_secuencias(i)
    print(izquierda, derecha)
# La línea 4 de test tiene el lado derecho incluido en el izquierdo PERO según
# el enunciado, solo la línea 5 tiene un rango incluido, es decir, han comprobado si 
# el intervalo de la IZQUIERDA se incluye en la DERECHA
#%% Iterar en el rango en la izquierda
# params: izquierda, derecha -> las dos secuencias de cada linea
# return: 1 si el rango izq está incluido en el der, 0 si no
def verificar_rango(izquierda, derecha):
    resultado = 0
    contador_izq = 0
    contador_der = 0
    for i in izquierda:
        if i in derecha:    
            contador_izq += 1
    if contador_izq < len(izquierda):
        for i in derecha:
            if i in izquierda:
                contador_der += 1
    if contador_izq == len(izquierda) or contador_der == len(derecha):
        resultado = 1
    return resultado
#%% Bucle para comprobar si las secuencias están incluidas en test.txt
datos_test = leer_txt('test-4.txt')
for i in datos_test:
    izquierda, derecha = reordenar_secuencias(i)
    print(verificar_rango(izquierda, derecha))
# correcto -> solo sale 1 en la línea 5 mirando de izq a der // ahora sale 1+1 = 2 mirando en ambos sentidos
#%% Bucle para sumar el contador de secuencias incluidas en test.txt
datos_test = leer_txt('test-4.txt')
contador = 0
for i in datos_test:
    izquierda, derecha = reordenar_secuencias(i)
    contador += verificar_rango(izquierda, derecha)
print(contador) # correcto -> 1 de izq a der y 2 en ambos sentidos
#%% Bucle en datos de input
datos_test = leer_txt('input-4.txt')
contador = 0
for i in datos_test:
    izquierda, derecha = reordenar_secuencias(i)
    contador += verificar_rango(izquierda, derecha)
print(contador) # 288 de izq a der y 479 en ambos sentidos
# El resultado CORRECTO es 500 pero nos sale 479
#%% --- Parte 2 ---
# Ahora miramos solapamiento parcial, al menos de un número
    # Ahora comprobamos si al menos un número está en ambas secuencias
def verificar_rango_parcial(izquierda, derecha):
    for i in izquierda:
        if i in derecha:    
            return 1
    for i in derecha:
        if i in izquierda:
            return 1
    return 0
#%% Bucle para comprobar si las secuencias están incluidas en test.txt
datos_test = leer_txt('test-4.txt')
contador = 0
for i in datos_test:
    izquierda, derecha = reordenar_secuencias(i)
    print(verificar_rango_parcial(izquierda, derecha))
    contador += verificar_rango_parcial(izquierda, derecha)
print("contador:", contador) # correcto -> 4
#%% Bucle en datos de input
datos_test = leer_txt('input-4.txt')
contador = 0
for i in datos_test:
    izquierda, derecha = reordenar_secuencias(i)
    contador += verificar_rango_parcial(izquierda, derecha)
print("contador:", contador) # 
# %%
