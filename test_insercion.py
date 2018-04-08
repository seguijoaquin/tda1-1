import unittest
from insercion import insercion

class Insercion(unittest.TestCase):
       
    def test_insercion(self):
        arreglo  = [2,5,6,17,4,66,34,1,18,29,12]
        final = [1,2,4,5,6,12,17,18,29,34,66]
        self.assertEqual(insercion(arreglo), final)
