import unittest
from heapsort import heapsort

class Heapsort(unittest.TestCase):
       
    def test_heapsort(self):
        arreglo  = [2,2,5,6,1,1,7,8]
        final =   [1,1,2,2,5,6,7,8]
        self.assertEqual(heapsort(arreglo), final)