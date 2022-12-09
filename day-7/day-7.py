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
#%% 2. Interpretamos comandos y lista de dirs y archivos
    # Comandos: empieza la línea por $
    # Directorios: empieza la línea por dir
    # Archivos: empieza la línea por int
tree = {}
root = "/"
pwd = []
dir_actual = ""
def interpretar_comandos(datos):
    for linea in datos:
        if linea[0] == "$":
            comando = linea.split(" ", 1)[1]
            # print("cmd:", comando)
            if comando.startswith("cd"):
                if comando.endswith(".."):
                    # lógica para ir a carpeta superior
                    navegar_a_parent()
                else:
                    # lógica para ir a carpeta inferior
                    navegar_a_child()
            elif comando.startswith("ls"):
                # tomar archivos o carpetas hasta encontrar otro comando
                guardar_archivos_o_dirs()
        elif linea.startswith("dir"):
            nombre_dir = linea.split(" ", 1)[1]
            crear_dict_de_dir(pwd, nombre_dir)
        elif linea.split(" ")[0].isdigit():
            guardar_archivo_en_dict()
interpretar_comandos(datos_test)
#%% Definimos funciones auxiliares
# Registra que hemos cambiado a la carpeta superior
def navegar_a_parent():
    pass
# Registra que hemos cambiado a una carpeta inferior
def navegar_a_child():
    pass
# Guarda los archivos o carpetas hasta encontrar otro comando
def guardar_archivos_o_dirs():
    pass
# Crea un diccionario
def crear_dict_de_dir(pwd, nombre_dir):
    el = tree.get(root)
    idx = 1
    while idx < len(pwd):
        key = pwd[idx]
        el = el.get(key)
        idx += 1
    if el.get(nombre_dir) is None:
        el[nombre_dir] = {}
    else: 
        pass
# Guarda un archivo en el diccionario de su carpeta
def guardar_archivo_en_dict():
    pass