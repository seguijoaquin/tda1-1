import unittest
from merge import merge, merge_sort

class Merge(unittest.TestCase):
       
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
