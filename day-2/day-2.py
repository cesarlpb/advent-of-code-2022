# Day 2 - https://adventofcode.com/2022/day/2

# Determinar ganador, empate o perdida
# Usando nuestra elección y el resultado -> puntuación
# Vamos sumando las puntuaciones

#%% Leer del input
input = ""
with open('input-2.txt', 'r') as f:
    input = f.read().splitlines()
print(input)
#%% Parte 1
punto = []
# Puntos según resultado
            # perder, empatar, ganar
puntos_resultado = [0, 3, 6]
# Oponente -> A: papel, B: tijeras, C: piedra
oponente = {'A': 'papel', 'B': 'tijeras', 'C': 'piedra'}
# Elección -> X: papel, Y: tijeras, Z: piedra
eleccion = {'X': 'papel', 'Y': 'tijeras', 'Z': 'piedra'}
# Lógica de juego
    # Piedra vence a Tijeras, Tijeras vence a Papel y Papel vence a Piedra
    # X Si el oponente es igual a la elección, es un empate
def juego(eleccion_oponente, eleccion_nuestra):
    if oponente.get(eleccion_oponente)  == eleccion.get(eleccion_nuestra):
        return 1    # empate -> índice 1 en puntos_resultado
    elif (oponente.get(eleccion_oponente) == 'piedra' and eleccion.get(eleccion_nuestra) == 'tijeras') or (oponente.get(eleccion_oponente) == 'tijeras' and eleccion.get(eleccion_nuestra) == 'papel') or (oponente.get(eleccion_oponente) == 'papel' and eleccion.get(eleccion_nuestra) == 'piedra'):
        return 0    # perder -> índice 0 en puntos_resultado
    else:
        return 2
# Puntos según elección