
################
# Tomas Grossi - @Ladrusca
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def analisis_anagrama(lista_palabras):
    
    diccionario_palabras = {}

    for palabra in lista_palabras: 

        palabra_diseccionadas = {}

        for letra in palabra:
            
            if letra != ' ':
                palabra_diseccionadas[letra.lower()] = 1

        diccionario_palabras[palabra] = palabra_diseccionadas

    
    for letra in diccionario_palabras[lista_palabras[0]].items():

        valor_letra = letra[1]
        letra = letra[0]

        for palabra_comparativa in diccionario_palabras.values():

            for letra_comparativa in palabra_comparativa.items():

                valor_letra_comparativa = letra_comparativa[1]
                letra_comparativa = letra_comparativa[0]

                if letra_comparativa == letra and valor_letra_comparativa != valor_letra:

                    return False

            
                
        
    return True
    


def principal():
    """Toda la interacción con el usuario va acá"""
    
    bucle = True
    lista_palabras = []

    while bucle:

        palabra = input('Ingrese una palabra: ')
        lista_palabras.append(palabra)

        opcion = input('ingresar otro palabra? s/n: ')
            
        if opcion == 'n':
            
            bucle = False
    
    es_anagrama = analisis_anagrama(lista_palabras)
    print(es_anagrama)



if __name__ == "__main__":
    principal()