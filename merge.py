#import logging
#logging.basicConfig(filename='merge.log', level=logging.DEBUG)

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

def merge_sort(vector):
    if len(vector) < 2:
        return vector
    izquierdo_ordenado = merge_sort(vector[:len(vector)//2])
    derecho_ordenado = merge_sort(vector[len(vector)//2:])
    return merge(izquierdo_ordenado, derecho_ordenado) 
