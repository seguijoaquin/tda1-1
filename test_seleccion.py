from seleccion import minimo, intercambia, seleccion, merge
import unittest

class Seleccion(unittest.TestCase):

    def test_minimo(self):
        arreglo = [2,4,5,0,3,7,1,2,5,6]
        self.assertEqual(minimo(arreglo), 3)

    def test_minmo_corrido(self):
        arreglo = [2,4,5,0,3,7,1,2,5,6]
        self.assertEqual(minimo(arreglo, 4), 6)

    def test_intercanbio(self):
        arreglo = [2,4,5,0,3,7,1,2,5,6]
        final = [2,4,5,0,7,3,1,2,5,6]
        intercambia(arreglo, 4,5)
        self.assertEqual(arreglo,final)

    def test_seleccion(self):
        arreglo = [2,4,5,0,3,7,1,2,5,6]
        final =   [0,1,2,2,3,4,5,5,6,7]
        self.assertEqual(seleccion(arreglo), final)
        
    def test_merge(self):
        arreglo  = [2,2,5,6]
        arreglo2 = [1,1,7,8]
        final =   [1,1,2,2,5,6,7,8]
        self.assertEqual(merge(arreglo,arreglo2), final)

    def test_merge_funciona_arreglo_vacio(self):
        arreglo  = []
        arreglo2 = [1,1,7,8]
        final = [1,1,7,8]
        self.assertEqual(merge(arreglo,arreglo2), final)
