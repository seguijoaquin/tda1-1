from heap import Heap

def heapsort(lista):
    heap = Heap(lista)
    lista_ordenada = []
    while len(heap) > 0:
        lista_ordenada.append(heap.pop())
    return lista_ordenada