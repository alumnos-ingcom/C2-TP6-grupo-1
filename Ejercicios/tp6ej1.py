################
# Matias Scandizzo - @matihkcs
# Plantilla de ejercicio Numero 1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def analisis_anagrama(palabra1, palabra2):
    '''Funcion para analizar posibles anagramas
'''

    dict_palabra1 = {}
    dict_palabra2 = {}

    for letra in palabra1:

        if letra != '':

            if dict_palabra1.get(letra) == None:        
                
                dict_palabra1[letra] = 1

            else:
            
                dict_palabra1[letra] += 1


    for letra in palabra2:
        
        if letra != '':

            if dict_palabra2.get(letra) == None:        
                
                dict_palabra2[letra] = 1

            else:
            
                dict_palabra2[letra] += 1

    '''Chequeo si la letra y la cantidad de veces que aparece es la misma'''
    for letra in dict_palabra1:

        if dict_palabra1.get(letra) != dict_palabra2.get(letra):

            return False

    return True

        
            
    


def principal():
        
    palabra1 = input('Ingrese una palabra: ')
    palabra2 = input('Ingrese otra palabra: ')
    
    es_anagrama = analisis_anagrama(palabra1, palabra2)
    
    print(es_anagrama)



if __name__ == "__main__":
    principal()