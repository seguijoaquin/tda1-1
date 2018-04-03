# coding: utf-8
import time
import random

def performance(vector, algoritmo):
    inicio = time.time()
    algoritmo(vector)
    return time.time()-inicio

def gen_vector(length):
    return [random.randrange(1000) for _ in range(length)]
