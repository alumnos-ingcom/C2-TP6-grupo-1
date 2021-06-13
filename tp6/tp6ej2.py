
################
# Tomas Grossi - @Ladrusca
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp6ej1 import analisis_anagrama

def identificador_palabras(archivo):
    '''Funcion para analizar un texto y separar las palabras'''

    lista_palabras = []

    archivo = open(archivo, encoding="utf8")
    
    texto = archivo
    texto = texto.readlines()

    archivo.close()

    for renglon in texto:

        palabra1 = ''
        palabra2 = ''

        separador = renglon.find('–')
        cierre = renglon.find("\n")

        for letra in renglon[:separador]:

            if letra != ' ':
                palabra1 += letra.lower()
        

        for letra in renglon[separador + 1:cierre]:

            if letra != ' ':
                palabra2 += letra.lower()

        lista_palabras.append([palabra1, palabra2])

    return lista_palabras


def principal():
    """Toda la interacción con el usuario va acá"""
    
    texto = '../anagramas.txt'
    
    lista_palabras = identificador_palabras(texto)

    for palabras in lista_palabras:

        print(palabras, analisis_anagrama(palabras[0], palabras[1]))



if __name__ == "__main__":
    principal()