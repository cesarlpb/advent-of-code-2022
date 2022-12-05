# Day 1 - https://adventofcode.com/2022/day/1

# Leer input de input-1.txt
# Leer los grupos de números separados por \n\n
# Cada grupo es un "elfo" que tiene que sumar los números
# Debemos registrar la suma de cada elfo -> "calorías" -> int
# Hallamos la suma máxima de calorías -> int

#%% Parte 1: leer input
with open('input-1.txt', 'r') as f:
    input = f.read().split('\n\n')
    print(input)