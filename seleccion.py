def minimo(vector, a_partir_de=0):
    if not bool(vector):
        return vector
    indice_min = a_partir_de
    for indice, valor in enumerate(vector[a_partir_de:]):
        if valor < vector[indice_min]:
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
