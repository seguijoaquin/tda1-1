#import logging
#logging.basicConfig(filename='merge.log', level=logging.DEBUG)

def merge(izquierdo, derecho):
    resultado = []
    i = 0
    j = 0
    while i < len(izquierdo) and j < len(derecho):
        if izquierdo[i] < derecho[j]:
            resultado.append(izquierdo[i])
            i+=1
        else:
            resultado.append(derecho[j])
            j+=1
    # Si quedan elementos en izquierdo los sumo
    if i < len(izquierdo):
        resultado += izquierdo[i:]
    # Si quedan elementos en derecho los sumo
    if j < len(derecho):
        resultado += derecho[j:]
    return resultado

def merge_sort(vector):
    if len(vector) < 2:
        return vector
    izquierdo_ordenado = merge_sort(vector[:len(vector)//2])
    derecho_ordenado = merge_sort(vector[len(vector)//2:])
    return merge(izquierdo_ordenado, derecho_ordenado) 
