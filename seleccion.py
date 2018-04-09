#import logging
#logging.basicConfig(filename='seleccion.log', level=logging.INFO)

def minimo(vector, a_partir_de=0):
    if not bool(vector):
        #logging.error('[*]ERROR el vector no debe ser vacio')
        return vector
    indice_min = a_partir_de
    for indice, valor in enumerate(vector[a_partir_de:]):
        if valor < vector[indice_min]:
            #logging.debug('indice_min era {}, y ahora es {}'.format(indice_min, indice))
            indice_min = indice + a_partir_de # corro el indice en caso de que sea necesario
    return indice_min

def intercambia(vector, indice_a, indice_b):
    vector[indice_a], vector[indice_b] = vector[indice_b], vector[indice_a]
    return vector

def seleccion(vector):
    for indice,valor in enumerate(vector[:-1]):
        indice_minimo = minimo(vector, a_partir_de=indice)
        intercambia(vector, indice, indice_minimo)
    return vector
