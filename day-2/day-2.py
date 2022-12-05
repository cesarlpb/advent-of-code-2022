# Day 2 - https://adventofcode.com/2022/day/2

# X Determinar ganador, empate o perdida
# X Usando nuestra elección y el resultado -> puntuación
# X Vamos sumando las puntuaciones

#%% Leer del input del txt
input = ""
with open('input-2.txt', 'r') as f:
    input = f.read().splitlines()
    # Opcional: quitar espacios en blanco
    for i in range(len(input)):
        input[i] = input[i].replace(' ', '')
# print(input) # lista de partidas jugadas, formato AY, BX, CZ, etc. Correcto
#%% Parte 1 - función que determina ganador, empate o perdida y retorna puntos
puntos = [] 
# Oponente -> A: piedra, B: papel, C: tijeras
oponente_dict = {'A': 'piedra', 'B': 'papel', 'C': 'tijeras'}
# Elección -> X: piedra, Y: papel, Z: tijeras
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
# print(puntos)     # test: [8, 1, 6]
print(sum(puntos))  # test: 15
#%% Parte 2 - Entendiendo que X, Y, Z significan que perdemos, empatamos o ganamos
# Recalculamos los puntos
oponente_dict = {'A': 'piedra', 'B': 'papel', 'C': 'tijeras'} # no cambia
eleccion_dict = {'X': 'perder', 'Y': 'empatar', 'Z': 'ganar'} # ahora entendemos esto a partir de X, Y, Z
# Debemos deducir que forma vamos a tomar para ganar, empatar o perder
casos_perder = {'piedra': 'tijeras', 'papel': 'piedra', 'tijeras': 'papel'}
casos_ganar = {'piedra': 'papel', 'papel': 'tijeras', 'tijeras': 'piedra'}
def resultado_a_forma(eleccion_oponente, resultado):
    # params: 
        # eleccion_oponente = A, B o C -> piedra, papel o tijeras
        # resultado = 0, 1 o 2 -> perder, empatar o ganar
    # Empate
    if resultado == 1:
        return oponente_dict.get(eleccion_oponente)
    # Ganar
    elif resultado == 2:
        return casos_ganar.get(oponente_dict.get(eleccion_oponente))
    # Perder
    elif resultado == 0:
        return casos_perder.get(oponente_dict.get(eleccion_oponente))
# Lógica de juego -> input es 0, 1 o 2 -> output: piedra, papel o tijeras
puntos = []
puntos_forma_elegida = {'piedra': 1, 'papel': 2, 'tijeras': 3}
puntos_resultado = {0: 0, 1: 3, 2: 6}
def calculo_de_puntos(forma_nuestra, resultado):
    # params: 
        # forma_nuestra = piedra, papel o tijeras
        # resultado = 0, 1 o 2 -> perder, empatar o ganar
    puntos.append(puntos_forma_elegida.get(forma_nuestra) + puntos_resultado.get(resultado))

#%% Tests
# Probamos resultado_a_forma
# Piedra
print("-- Piedra --")
print(resultado_a_forma('A', 1)) # piedra
print(resultado_a_forma('A', 2)) # papel
print(resultado_a_forma('A', 0)) # tijeras
# Papel
print("\n-- Papel --")
print(resultado_a_forma('B', 1)) # papel
print(resultado_a_forma('B', 2)) # tijeras
print(resultado_a_forma('B', 0)) # piedra
# Tijeras
print("\n-- Tijeras --")
print(resultado_a_forma('C', 1)) # tijeras
print(resultado_a_forma('C', 2)) # piedra
print(resultado_a_forma('C', 0)) # papel
# Todo correcto
#%% Bucle que recalcula los nuevos puntos
nuevo_eleccion_dict = {'X': 0, 'Y': 1, 'Z': 2}
for partida in input:
    calculo_de_puntos(resultado_a_forma(partida[0], nuevo_eleccion_dict.get(partida[1])), nuevo_eleccion_dict.get(partida[1]))
# print(puntos) # comprobamos el primero, correcto
print(sum(puntos))