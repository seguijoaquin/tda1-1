# A es el conjunto que propone
# B es el conjunto que recibe propuestas

# conjuntoA es una lista de enteros que representa todos los equipos
# conjuntoB es una lista de enteros que representa todos los jugadores
# preferenciasConjuntoA es un diccionario donde:
#         clave = elemento del conjunto A (un equipo)
#         valor = una lista donde:
#                    posicion 0 = lista de preferencias de A invertida (del jugador menos preferido al mas preferido)
#                    posicion 1 = un diccionario donde:
#                                     clave = elemento de B (un jugador)
#                                     valor = posicion en la lista de preferencias de A (si 15 es el jugador mas preferido del equipo 2, habria un "15:1")
# preferenciasConjuntoB es lo mismo que preferenciasConjuntoA pero intercambiando equipo por jugador y A por B en la descripcion
# lenVacantesDeElementoA es la cantidad de elementos de B que se le puede asignar a un elemento de A (un equipo tiene 10 jugadores => lenVacantesDeElementoA = 10)
def galeshapley(conjuntoA, conjuntoB, preferenciasConjuntoA, preferenciasConjuntoB, lenVacantesDeElementoA):
    ocupadosDeB = {}
    seleccion = {}
    while len(conjuntoA) > 0:
        elementoA = conjuntoA.pop()
        # Saco el elemento mas preferido de A que no haya sido evaluado
        elementoB = preferenciasConjuntoA[elementoA][0].pop()
        # Si no esta ocupado
        if not ocupadosDeB.__contains__(elementoB):
            # Lo inserto en la seleccion final
            if not seleccion.__contains__(elementoA):
                seleccion.__setitem__(elementoA, {elementoB})
            else:
                seleccion.get(elementoA).add(elementoB)
            # Lo marco como ocupado
            ocupadosDeB.__setitem__(elementoB, elementoA)
        # Si esta ocupado
        else:
            # Obtengo quien lo esta ocupando
            elementoDeAAsignado = ocupadosDeB.get(elementoB)
            # Si B prefiere la propuesta de A antes que la propuesta que ya tenia
            if preferenciasConjuntoB[elementoB][1].get(elementoDeAAsignado) > preferenciasConjuntoB[elementoB][1].get(elementoA):
                # El A se queda con el B
                if not seleccion.__contains__(elementoA):
                    seleccion.__setitem__(elementoA, {elementoB})
                else:
                    seleccion.get(elementoA).add(elementoB)
                ocupadosDeB.__setitem__(elementoB, elementoA)
                # El A anterior se queda sin el B
                seleccion[elementoDeAAsignado].discard(elementoB)
                # Si el A anterior ya estaba completo
                if len(seleccion[elementoDeAAsignado]) == (lenVacantesDeElementoA - 1):
                    # Vuelve a tener que buscar otros B para completar
                    conjuntoA.append(elementoDeAAsignado)
        # Si A no tiene ningun B o tiene Bs pero no esta completo
        if not seleccion.__contains__(elementoA) or len(seleccion[elementoA]) < lenVacantesDeElementoA :
            # Sigue en la busqueda de Bs
            conjuntoA.append(elementoA)
    print(seleccion)            
    