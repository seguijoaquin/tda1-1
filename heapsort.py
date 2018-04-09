from heap import Heap

def heapsort(lista):
    heap = Heap(lista)
    lista_ordenada = []
    while heap.size() > 0:
        lista_ordenada.append(heap.pop())
    return lista_ordenada