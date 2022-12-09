# Estructura de datos
    # Diccionario -> carpetas y archivos
        # Lista -> archivos en carpeta
        # tupla (int, str) -> cada archivo
# my_dict: {
# "/": {
#   "dir a": {
#       "dir e": {
#           "i": 584
#           }, 
#       "f": 1212 
#       "g": 2557, 
#       "h.lst": 62596
#      },
#  "dir d": {
#       "j": 4060174
#       "d.log":  8033020,
#       "d.ext": 5626152,
#       "k": 7214296
#    }
# }
# carpeta -> dict
# archivo -> tupla (int, str)
# Diagrama de los directorios y archivos

# Parte 1 - Crear diccionario con directorios y archivos
#%% 1. Leer txt de test
def leer_txt(archivo):
    with open(archivo, 'r') as f:
        datos = f.read().splitlines()
    return datos
datos_test = leer_txt('test-7.txt')
#%% Definimos funciones auxiliares
# Navegar a la key del elemento en tree
def navegar_a_key(pwd):
    # if tree.get(root) is None:
    #     tree[root] = {}
    el = tree.get(root)
    print("el:", el)
    idx = 1
    while idx < len(pwd):
        key = pwd[idx]
        el = el.get(key)
        idx += 1
    return el
# Registra que hemos cambiado a la carpeta superior
def navegar_a_parent(pwd):
    pwd.pop()

# Registra que hemos cambiado a una carpeta inferior
def navegar_a_child(pwd, nombre_dir):
    el = navegar_a_key(pwd)
    print("nombre_dir desde nav_child:", nombre_dir)
    if el is None:
        tree[nombre_dir] = {}
    pwd.append(nombre_dir)

# Guarda los archivos o carpetas hasta encontrar otro comando
def guardar_archivos_o_dirs():
    pass
# Crea un diccionario
def crear_dict_de_dir(pwd, nombre_dir):
    el = tree.get(root)
    # print("el:", el)
    idx = 1
    while idx < len(pwd):
        key = pwd[idx]
        print("key:", key, "el:", el)
        temp = el.get(key)
        if temp is None:
            el[nombre_dir] = {}
        print("el:", el)
        idx += 1
    else: 
        pass
# Guarda un archivo en el diccionario de su carpeta
def guardar_archivo_en_dict(size, nombre_archivo):
    # navegar a la posición actual en el dict
    # guardar archivo como size: nombre_archivo
    if navegar_a_key(pwd).get(nombre_archivo) is None:
        navegar_a_key(pwd)[size] = nombre_archivo
#%% 2. Interpretamos comandos y lista de dirs y archivos
    # Comandos: empieza la línea por $
    # Directorios: empieza la línea por dir
    # Archivos: empieza la línea por int
tree = {}
root = "/"
pwd = []
def interpretar_comandos(datos):
    for linea in datos:
        if linea[0] == "$":
            comando = linea.split(" ", 1)[1]
            # print("cmd:", comando)
            if comando.startswith("cd"):
                if comando.endswith(".."):
                    # lógica para ir a carpeta superior
                    navegar_a_parent(pwd)
                else:
                    # lógica para ir a carpeta inferior
                    nombre_dir = linea.split(" ", 2)[-1]
                    navegar_a_child(pwd, nombre_dir)
            elif comando.startswith("ls"):
                # tomar archivos o carpetas hasta encontrar otro comando
                # guardar_archivos_o_dirs()
                pass
        elif linea.startswith("dir"):
            nombre_dir = linea.split(" ", 1)[1]
            print(pwd, nombre_dir)
            crear_dict_de_dir(pwd, nombre_dir)
        elif linea.split(" ")[0].isdigit():
            [size, nombre_archivo] = linea.split(" ")
            guardar_archivo_en_dict(size, nombre_archivo)
interpretar_comandos(datos_test)
# %% Comprobamos SI el size es único en el input
def comprobar_size_unico():
    datos_input = leer_txt('input-7.txt')
    lista_de_archivos = []
    for linea in datos_input:
        if linea.split(" ")[0].isdigit():
            [size, nombre_archivo] = linea.split(" ")
            lista_de_archivos.append((size, nombre_archivo))
    new_set = set(lista_de_archivos)
    print("lista completa:", len(lista_de_archivos))
    print("set:", len(new_set))
comprobar_size_unico() # 294 y 294 => SI es único el size. El nombre_archivo si se repite pero en combinación ambos datos son únicos
# %% # Resolver el problema con dir a -> que no se está añadiendo bien al dict
