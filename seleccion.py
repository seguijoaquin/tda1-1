import logging
logging.basicConfig(filename='ordenamiento.log', level=logging.DEBUG)

def minimo(vector, a_partir_de=0):
    if not bool(vector):
        logging.error('[*]ERROR el vector no debe ser vacio')
        return vector
    indice_min = a_partir_de
    for indice, valor in enumerate(vector[a_partir_de:]):
        if valor < vector[indice_min]:
            logging.debug('indice_min era {}, y ahora es {}'.format(indice_min, indice))
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

def merge(izquierdo, derecho):
    resultado = []
    while izquierdo and derecho:
        if izquierdo[0] < derecho[0]:
            resultado.append(izquierdo[0])
            izquierdo.remove(izquierdo[0])
        else:
            resultado.append(derecho[0])
            derecho.remove(derecho[0])
    if not izquierdo:
        resultado += derecho
    if not derecho:
        resultado += izquierdo
    return resultado
