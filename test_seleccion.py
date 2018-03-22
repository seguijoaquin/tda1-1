from seleccion import minimo
import unittest

class Seleccion(unittest.TestCase):

    def test_minimo(self):
        arreglo = [2,4,5,0,3,7,1,2,5,6]
        self.assertEqual(minimo(arreglo), 3)

    def test_minmo_corrido(self):
        arreglo = [2,4,5,0,3,7,1,2,5,6]
        self.assertEqual(minimo(arreglo, 4), 6)

        
