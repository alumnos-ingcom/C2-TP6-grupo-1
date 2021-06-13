
################
# Tomas Grossi - @Ladrusca
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def hace_etiqueta(contenido, etiqueta, atributos = None):
    '''Funcion para crear una etiqueta'''

    nueva_etiqueta = f'<{etiqueta}'

    if atributos != None:
        for atributo in atributos:

            nuevo_atributo = ' ' + atributo + ' = "' + atributos.get(atributo) + '" '
            nueva_etiqueta += nuevo_atributo 

    nueva_etiqueta += f'>{contenido}</{etiqueta}>'

    return nueva_etiqueta

def hace_comenta(contenido):
    '''Funcion para crear el elemento comentario'''

    nuevo_comentario = f'<!-- {contenido} -->' 

    return nuevo_comentario


def creador_pagina():
    '''Funcion para crear elementos de la pagina'''

    e_h1 = hace_etiqueta('Hola HTML','h1', {'style':'color: red;', 'id':'titulo_principal'})
    e_parrafo = hace_etiqueta('Esto es un parrafo','p')
    e_boton = hace_etiqueta('ir a google','button', {'style':'color: white; background-color: blue;'})
    e_comentario = hace_comenta('Este es un comentario!')

    e_link = hace_etiqueta(e_boton, 'a', {'href':'https://www.google.com'})
    e_body = hace_etiqueta(e_h1 + e_parrafo + e_comentario + e_link,'body')
    e_html = hace_etiqueta(e_body,'html')

    pagina = e_html

    return pagina

def manejador_archivo(texto, nombre_archivo):
    '''Funcion para crear y escribir el archivo de salida'''

    nuevo_archivo = open(nombre_archivo + '.html', "w")

    nuevo_archivo.write(texto)

    nuevo_archivo.close()

def principal():
    """Toda la interacción con el usuario va acá"""
    
    texto = creador_pagina()

    manejador_archivo(texto, 'pagina')

if __name__ == "__main__":
    principal()