# Day 2 - https://adventofcode.com/2022/day/2

# Determinar ganador, empate o perdida
# Usando nuestra elección y el resultado -> puntuación
# Vamos sumando las puntuaciones

#%% Leer del input
input = ""
with open('test.txt', 'r') as f:
    input = f.read().splitlines()
    # Opcional: quitar espacios en blanco
    for i in range(len(input)):
        input[i] = input[i].replace(' ', '')
print(input) # lista de partidas jugadas, formato AY, BX, CZ, etc. Correcto
#%% Parte 1 - función que determina ganador, empate o perdida y retorna puntos
puntos = [] 
# Puntos según resultado
            # perder, empatar, ganar
puntos_resultado = [0, 3, 6]
# Oponente -> A: papel, B: tijeras, C: piedra
oponente_dict = {'A': 'piedra', 'B': 'papel', 'C': 'tijeras'}
# Elección -> X: papel, Y: tijeras, Z: piedra
eleccion_dict = {'X': 'piedra', 'Y': 'papel', 'Z': 'tijeras'}
# Lógica de juego
    # Piedra vence a Tijeras, Tijeras vence a Papel y Papel vence a Piedra
    # X Si el oponente es igual a la elección, es un empate
def juego(oponente, nosotros):
    eleccion_oponente = oponente_dict.get(oponente)  # A, B o C
    eleccion_nuestra = eleccion_dict.get(nosotros)  # X, Y o Z
    # Caso de empate -> índice 1 en puntos_resultado
    if eleccion_oponente  == eleccion_nuestra:
        return 1    
    # Caso de perder -> índice 0 en puntos_resultado
    # Rehacer esto comparando dos listas
    elif (eleccion_oponente == 'piedra' and eleccion_nuestra == 'tijeras') or (eleccion_oponente == 'tijeras' and eleccion_nuestra == 'papel') or (eleccion_oponente == 'papel' and eleccion_nuestra == 'piedra'):
        return 0    # perder -> índice 0 en puntos_resultado
    # Caso de ganar -> índice 2 en puntos_resultado
    else:
        return 2
#%% Test de test.txt
# Sabemos que test.txt tiene datos que suman 15 según las reglas de puntos del juego
    # A Y   papel=2   2+6 = 8
    # B X   piedra=1  1+0 = 1
    # C Z   tijeras=3 3+3 = 6
    # Total = 15
puntos = []
nuestras_elecciones = []
eleccion = {'X': 'piedra', 'Y': 'papel', 'Z': 'tijeras'}
for partida in input: 
    oponente = partida[0] # A, B o C
    nosotros = partida[1] # X, Y o Z
    nuestras_elecciones.append(nosotros)
    puntos.append(juego(oponente, nosotros))
    # print("partida:", partida)
    # print("puntos:", puntos) 
    puntos_forma_elegida = {'piedra': 1, 'papel': 2, 'tijeras': 3}
    puntos_resultado = {0: 0, 1: 3, 2: 6}
# puntos esta correcto
# suma de puntos de forma elegida y resultado
for i in range(len(puntos)):
    nuestra_eleccion = eleccion.get(nuestras_elecciones[i]) # fix -> esto ahora va cambiando según cada partida
    puntos_forma = puntos_forma_elegida.get(nuestra_eleccion)
    puntos_res = puntos_resultado.get(puntos[i])
    puntos[i] = puntos_forma + puntos_res # 2+6 = 8, 1+0 = 1, 3+3 = 6 -> 15
    # print(puntos[i], puntos_forma, puntos_res)    # cuadra todo
print(puntos)       # [8, 1, 6]
print(sum(puntos))  # 15
# Puntos según elección