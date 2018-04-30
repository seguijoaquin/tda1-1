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

    def test_merge_sort(self):
        arreglo = [2,4,5,0,3,7,1,2,5,6]
        final =   [0,1,2,2,3,4,5,5,6,7]
        self.assertEqual(merge_sort(arreglo), final)
