import unittest
from quicksort import quicksort

class Quicksort(unittest.TestCase):

	def test_quicksort(self):
		arreglo = [2,8,4,1,3,5,9,12,7,6,10,11]
		final = [1,2,3,4,5,6,7,8,9,10,11,12]
		self.assertEqual(quicksort(arreglo), final)

