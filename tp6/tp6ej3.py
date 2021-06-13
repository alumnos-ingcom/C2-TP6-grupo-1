
################
# Tomas Grossi - @Ladrusca
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def copiadora(archivo_entrada, archivo_salida):
    '''Funcion para copiar un archivo en otro'''

    archivo_entrada = open(archivo_entrada, encoding="utf8")
    texto = archivo_entrada.read()
    archivo_entrada.close()


    archivo_salida = open(archivo_salida, "w")
    archivo_salida.write(texto)
    archivo_salida.close()


def principal():
    """Toda la interacción con el usuario va acá"""
    
    a_entrada = input("Ingrese direccion de archivo de entrada(ej: ../anagramas.txt): ")
    a_salida = input("Ingrese direccion de archivo de salida: ")

    copiadora(a_entrada, a_salida)

if __name__ == "__main__":
    principal()