################
# Matias Scandizzo - @matihkcs
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def codificador(texto, cant_rotacion):
    """Funcion para codificar 
"""
    
    texto_unicode = ''
    cant_rotacion = int(cant_rotacion)


    for letra in texto:

        letra_unicode = ord(letra)
        letra_codificada = ord(letra)


        for posicion in range(cant_rotacion):

            if letra_unicode <= 57:
                
                letra_codificada += 1

                if letra_codificada > 57:
                   
                    letra_codificada = 48

            elif letra_unicode <= 122:

                letra_codificada += 1

                if letra_codificada > 122:
                    
                    letra_codificada = 97

        
        texto_unicode += str(chr(letra_codificada))
        
    return texto_unicode



def decodificador(codigo, cant_rotacion):
    """Funcion para decodificar
"""
     
    texto_decodificado = ''
    cant_rotacion = int(cant_rotacion)


    for digito in codigo:

        letra_unicode = ord(digito)
        letra_decodificada = ord(digito)

        for posicion in range(cant_rotacion):

            if digito == '/':

                letra_decodificada = 32

            elif letra_unicode <= 57:
                
                letra_decodificada -= 1

                if letra_decodificada < 48:
                   
                    letra_decodificada = 57

            elif letra_unicode <= 122:

                letra_decodificada -= 1

                if letra_decodificada < 97:
                    
                    letra_decodificada = 122


        texto_decodificado += str(chr(letra_decodificada))
        
    return texto_decodificado



def prueba():
    
    bucle = True

    while bucle:

        opcion = input("1) Codificar 2) decodificar 3) salir ")

        if opcion == "1":
            texto = input("Ingrese un texto a codificar ")
            cant_rotacion = input("Ingrese cuantas veces debe rotar ")
            texto = codificador(texto, cant_rotacion)
            print(texto)

        if opcion == "2":          
            texto = input("Ingrese un texto a decodificar ")
            cant_rotacion = input("Ingrese la cantidad de rotacion ")
            texto = decodificador(texto, cant_rotacion)
            print(texto)

        if opcion == "3":
            bucle = False

if __name__ == "__main__":
    prueba()

