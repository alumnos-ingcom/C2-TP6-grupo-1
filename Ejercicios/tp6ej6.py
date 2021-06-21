################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def hace_etiqueta(contenido, etiqueta):
    '''Funcion para crear una etiqueta'''

    nueva_etiqueta = f'<{etiqueta}>{contenido}</{etiqueta}>' 

    return nueva_etiqueta

def hace_comenta(contenido):
    '''Funcion para crear el elemento comentario'''

    nuevo_comentario = f'<!-- {contenido} -->' 

    return nuevo_comentario


def creador_pagina():
    '''Funcion para crear elementos de la pagina'''

    e_h1 = hace_etiqueta('Hola HTML','h1')
    e_parrafo = hace_etiqueta('Esto es un parrafo','p')
    e_boton = hace_etiqueta('esto es un boton','button')
    e_comentario = hace_comenta('Este es un comentario!')
    e_body = hace_etiqueta(e_h1 + e_parrafo + e_comentario + e_boton,'body')
    e_html = hace_etiqueta(e_body,'html')

    texto_pagina = e_html

    return texto_pagina

def manejador_archivo(texto, nombre_archivo):
    '''Funcion para crear y escribir el archivo de salida'''

    nuevo_archivo = open(nombre_archivo + '.html', "w")

    nuevo_archivo.write(texto)

    nuevo_archivo.close()

def principal():
    """Toda la interacción con el usuario va acá"""
    
    nombre_archivo = input("Ingrese un nombre para el archivo a guardar: ")

    texto = creador_pagina()

    manejador_archivo(texto, nombre_archivo)

if __name__ == "__main__":
    principal()