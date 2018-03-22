import logging
logger = logging.getLogger()

def minimo(vector, a_partir_de=0):
    if not bool(vector):
        logger.error('[*]ERROR el vector no debe ser vacio')
        return vector
    indice_min = a_partir_de
    for indice, valor in enumerate(vector[a_partir_de:]):
        if valor < vector[indice_min]:
            logger.info('indice_min era {}, y ahora es {}'.format(indice_min, indice))
            indice_min = indice 
    return indice_min + a_partir_de # corro el indice en caso de que sea necesario

def intercambia(vector, indice_a, indice_b):
    vector[indice_a], vector[indice_b] = vector[indice_b], vector[indice_a]
    return vector

def seleccion(vector):
    for indice,valor in enumerate(vector[:-1]):
        intercambia(vector, indice, minimo())
