import unittest
from galeshapley import galeshapley


class Galeshapley(unittest.TestCase):
       
    #def test_galeshapley(self):
    #    conjuntoA = [1, 2, 3, 4]
    #    conjuntoB = [1, 2, 3, 4]
    #    preferenciasA = {1 : [[4, 3, 1, 2], {2:1, 1:2, 3:3, 4:4}], 2 : [[3, 2, 1, 4], {4:1, 1:2, 2:3, 3:4}], 3 : [[4, 2, 3, 1], {1:1, 3:2, 2:3, 4:4}], 4 : [[4, 1, 3, 2], {2:1, 3:2, 1:3, 4:4}]}
    #    preferenciasB = {1 : [[4, 2, 3, 1], {1:1, 3:2, 2:3, 4:4}], 2 : [[2, 1, 4, 3], {3:1, 4:2, 1:3, 2:4}], 3 : [[1, 3, 2, 4], {4:1, 2:2, 3:3, 1:4}], 4 : [[4, 1, 2, 3], {3:1, 2:2, 1:3, 4:4}]}
    #    galeshapley(conjuntoA,conjuntoB,preferenciasA,preferenciasB, 1)
    #    self.assertEqual(1, 1)
        
    def test_galeshapley_archivos(self):
        conjuntoA = [i+1 for i in range(20)]
        conjuntoB = [i+1 for i in range(200)]
        preferenciasA = {}
        preferenciasB = {}
        for i in conjuntoA:
            preferenciasA.__setitem__(i, [[],{}])
            with open('galeshapley_test_files/equipo_' + i.__str__() +'.csv', 'r') as f:
                pref = f.readline().split(',')
                k = 200
                for j in reversed(pref):
                    preferenciasA[i][0].append(int(j))
                    preferenciasA[i][1].__setitem__(int(j), k)
                    k = k-1
        
        for i in conjuntoB:
            preferenciasB.__setitem__(i, [[],{}])
            with open('galeshapley_test_files/jugador_' + i.__str__() +'.csv', 'r') as f:
                pref = f.readline().split(',')
                k = 20
                for j in reversed(pref):
                    preferenciasB[i][0].append(int(j))
                    preferenciasB[i][1].__setitem__(int(j), k)
                    k = k-1
        
        galeshapley(conjuntoA,conjuntoB,preferenciasA,preferenciasB, 10)
