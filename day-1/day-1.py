# Day 1 - https://adventofcode.com/2022/day/1

# X Leer input de input-1.txt
# X Leer los grupos de números separados por \n\n
# Cada grupo es un "elfo" que tiene que sumar los números
# Debemos registrar la suma de cada elfo -> "calorías" -> int
# Hallamos la suma máxima de calorías -> int

#%% Parte 1: leer input
input = ""
with open('input-1.txt', 'r') as f:
    input = f.read().split('\n\n')
    f.close()   # Se cierra automático pero por si acaso
# print(input)    # txt -> lista de strings (cada string es un "elfo")
#%% Parte 2: procesar input -> sumamos cada grupo y lo guardamos en una lista
calorias = []
for grupo in input:
    calorias.append(sum([int(x) for x in grupo.split()]))
#%% Parte 3: hallamos la suma máxima de calorías
maximo = max(calorias)
print("Máximo:", maximo)
#%% Segunda parte - hallamos las 3 máximas calorías y la suma de ellas
topThree = sorted(calorias, reverse=True)[:3]
print("Top 3:", topThree) # lista con los 3 máximos
sum = sum(topThree)
print("Suma del top 3:", sum)      # suma de los 3 máximos